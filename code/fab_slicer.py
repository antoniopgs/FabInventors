from shapely.geometry import LineString, MultiLineString
from shapely.ops import split
import matplotlib.pyplot as plt
from fab_parser import parse

# COLOR NAMES: https://matplotlib.org/3.1.0/gallery/color/named_colors.html
colors = {
    "SETUP": "orange",
    "SUPPORT": "blue",
    "TRAVEL": "black",
    "SKIRT": "green",
    "WALL-OUTER": "red",
    "WALL-INNER": "cyan",
    "SKIN": "magenta",
    "FILL": "gold"
}

samples_folder = "./../gcode_samples/"
gcode_file = samples_folder + "1_peca.gcode"

def detect_boundaries(json):
    for i, point in enumerate(line["points"][1] for line in json["lines"]):
        if i != 0:
            if point[0] < min_x:
                min_x = point[0]
            elif point[0] > max_x:
                max_x = point[0]
            if point[1] < min_y:
                min_y = point[1]
            elif point[1] > max_y:
                max_y = point[1]
        else:
            min_x, max_x = point[0], point[0]
            min_y, max_y = point[1], point[1]

    return (min_x, max_x), (min_y, max_y)

def slice_json(json):
    detections = detect_boundaries(json)
    
    min_x, max_x = detections[0][0], detections[0][1]
    min_y, max_y = detections[1][0], detections[1][1]
    
    slice_amount = 3
    
    slice_width = (max_x - min_x) / slice_amount
    slice_depth = max_y - min_y

    boundary_1 = LineString([(min_x + slice_width, min_y), (min_x + slice_width, max_y)])
    boundary_2 = LineString([(max_x - slice_width, min_y), (max_x - slice_width, max_y)])

    boundaries = MultiLineString([boundary_1, boundary_2])

    fig = plt.figure()
    ax = fig.gca(projection="3d")

    for boundary in list(boundaries.geoms):
        boundary_coordinates = list(boundary.coords)
        
        bx1 = boundary_coordinates[0][0]
        by1 = boundary_coordinates[0][1]
        
        bx2 = boundary_coordinates[1][0]
        by2 = boundary_coordinates[1][1]
        
        ax.plot((bx1, bx2), (by1, by2), color="gray")

    for line in json["lines"]:
        lx1, ly1 = line["points"][0][0], line["points"][0][1]
        lx2, ly2 = line["points"][1][0], line["points"][1][1]
        
        line_str = LineString([(lx1,ly1), (lx2,ly2)])
        result = split(line_str, boundaries)

        for i, subline in enumerate(list(result.geoms)):
            subline_coordinates = list(subline.coords)
            
            sx1 = subline_coordinates[0][0]
            sy1 = subline_coordinates[0][1]
            
            sx2 = subline_coordinates[1][0]
            sy2 = subline_coordinates[1][1]

            if sx1 <= (min_x + slice_width) and sx2 <= (min_x + slice_width):
                ax.plot(
                    [sx1, sx2],
                    [sy1, sy2],
                    [line["points"][0][2], line["points"][1][2]],
                    color = colors[line["type"]]
                )   


    fig.show()

slice_json(parse(gcode_file))

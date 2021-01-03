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

def slice_json(json, slices = 3):
    fig = plt.figure()
    ax = fig.gca(projection="3d")
    
    min_x = min(line["points"][1][0] for line in json["lines"])
    max_x = max(line["points"][1][0] for line in json["lines"])
    
    min_y = min(line["points"][1][1] for line in json["lines"])
    max_y = max(line["points"][1][1] for line in json["lines"])
    
    slice_width = (max_x - min_x) / slices
    boundaries = []

    for i in range(1, slices):
        boundary = LineString([(min_x + i*slice_width, min_y), (min_x + i*slice_width, max_y)])
        boundaries.append(boundary)

        # To Visualize:
        bound_coords = list(boundary.coords)
        bx1, by1, bx2, by2 = bound_coords[0][0], bound_coords[0][1], bound_coords[1][0], bound_coords[1][1]
        ax.plot((bx1, bx2), (by1, by2), color="gray")

    boundaries = MultiLineString(boundaries)

    for line in json["lines"]:
        lx1, ly1 = line["points"][0][0], line["points"][0][1]
        lx2, ly2 = line["points"][1][0], line["points"][1][1]
        
        line_str = LineString([(lx1,ly1), (lx2,ly2)])
        sublines = split(line_str, boundaries)

        for subline in list(sublines.geoms):
            subline_coords = list(subline.coords)
            
            sx1 = subline_coords[0][0]
            sy1 = subline_coords[0][1]
            
            sx2 = subline_coords[1][0]
            sy2 = subline_coords[1][1] 

            if sx1 <= (min_x + slice_width) and sx2 <= (min_x + slice_width):
                ax.plot(
                    [sx1, sx2],
                    [sy1, sy2],
                    [line["points"][0][2], line["points"][1][2]],
                    color = colors[line["type"]]
                )   

    return fig

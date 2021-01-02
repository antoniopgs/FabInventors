from shapely.geometry import LineString, MultiLineString
from shapely.ops import split
from fab_visualizer import visualize
import matplotlib.pyplot as plt
from fab_parser import parse

samples_folder = "./../gcode_samples/"
g_code = samples_folder + "1_peca.gcode"
json = parse(g_code)

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

slice_amount = 3
slice_width = (max_x - min_x) / slice_amount
slice_depth = max_y - min_y

boundary_1 = LineString([(min_x + slice_width, min_y), (min_x + slice_width, max_y)])
boundary_2 = LineString([(max_x - slice_width, min_y), (max_x - slice_width, max_y)])
        

fig = visualize(json)
ax = fig.gca(projection="3d")

splitter = MultiLineString([boundary_1, boundary_2])

for boundary in list(splitter.geoms):
    boundary_coordinates = list(boundary.coords)
    
    x1 = boundary_coordinates[0][0]
    y1 = boundary_coordinates[0][1]
    
    x2 = boundary_coordinates[1][0]
    y2 = boundary_coordinates[1][1]
    
    ax.plot((x1, x2), (y1, y2), color="gray")

line = LineString([(0,20), (120,20)])
result = split(line, splitter)

for i, subline in enumerate(list(result.geoms)):
    subline_coordinates = list(subline.coords)
    
    x1 = subline_coordinates[0][0]
    y1 = subline_coordinates[0][1]
    
    x2 = subline_coordinates[1][0]
    y2 = subline_coordinates[1][1]
                                
    ax.plot((x1, x2), (y1, y2), color = "red" if i % 2 == 0 else "blue")

fig.show()

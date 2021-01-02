from shapely.geometry import LineString, MultiLineString
from shapely.ops import split
from fab_visualizer import visualize
import matplotlib.pyplot as plt
from fab_parser import parse

samples_folder = "./../gcode_samples/"
g_code = samples_folder + "1_peca.gcode"
json = parse(g_code)

fig = visualize(json)
ax = fig.gca(projection="3d")

boundary_1 = LineString([(40,0), (40,40)])
boundary_2 = LineString([(80,0), (80,40)])

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

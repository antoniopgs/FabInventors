import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
from fab_parser import parse
import os, json

samples_folder = os.getcwd().strip("code") + "gcode_samples"
file_names = os.listdir(samples_folder)

color_dict = {
    "SUPPORT": mcolors.to_rgba("blue"),
    "NONMESH": mcolors.to_rgba("green"),
    "TRAVEL": mcolors.to_rgba("green"),
    "SKIRT": mcolors.to_rgba("green"),
    "MESH_NAME": mcolors.to_rgba("red"),
    "WALL-OUTER": mcolors.to_rgba("orange"),
    "WALL-INNER": mcolors.to_rgba("orange"),
    "SKIN": mcolors.to_rgba("violet"),
    "FILL": mcolors.to_rgba("yellow")
}

for file_name in file_names:
    layers = json.loads(parse(f"{samples_folder}/{file_name}"))
    x, y, z, colors = [], [], [], []

    for value in layers.values():
        for line in value["lines"]:
            for point in line["Points"]:
                x.append(point[0])
                y.append(point[1])
                z.append(value["z"])
                colors.append(color_dict[line["Line Type"]])

    fig = plt.figure()
    ax = fig.gca(projection="3d")
    ax.set_title(file_name)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.plot(x, y, z)
    plt.show()

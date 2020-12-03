import matplotlib.pyplot as plt
from fab_parser import parse
import os, json

samples_folder = os.getcwd().strip("code") + "gcode_samples"
file_names = os.listdir(samples_folder)

for file_name in file_names:
    layers = json.loads(parse(f"{samples_folder}/{file_name}"))
    x, y, z = [], [], []

    for value in layers.values():
        for line in value["lines"]:
            for point in line["Points"]:
                x.append(point[0])
                y.append(point[1])
                z.append(value["z"])
                 
    fig = plt.figure()
    ax = fig.gca(projection="3d")
    ax.set_title(file_name)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.plot(x, y, z)
    plt.show()



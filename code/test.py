import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d as mpl
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
                      
    mpl.rcParams["legend.fontsize"] = 10
    fig = plt.figure()
    ax = fig.gca(projection="3d")
    ax.plot(x, y, z, label=file_name)
    ax.legend()
    plt.show()



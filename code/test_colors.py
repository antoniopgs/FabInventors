from fab_parser import parse
import matplotlib.pyplot as plt
import os

samples_folder = os.getcwd().strip("code") + "gcode_samples"
data = parse(f"{samples_folder}/1_peca.gcode")

colors = {
    "SUPPORT": "b", #blue
    "NONMESH": "g", #green
    "TRAVEL": "g", #green
    "SKIRT": "g", #green
    "MESH_NAME": "r", #red
    "WALL-OUTER": "c", #cyan
    "WALL-INNER": "c", #cyan
    "SKIN": "m", #magenta
    "FILL": "y", #yellow
}

fig = plt.figure()
ax = fig.gca(projection='3d')

x, y, z = [], [], []
c = ""
for layer in data["layers"].values():
    for line in layer["lines"]:
        c += colors[line["Line Type"]]
        for point in line["Points"]:
            x.append(point[0])
            y.append(point[1])
            z.append(layer["z"])

for i in range(len(x)):
    ax.plot(x[i:i+2], y[i:i+2], z[i:i+2], color=c[i%len(c)])

plt.show()

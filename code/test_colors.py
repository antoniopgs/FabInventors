import matplotlib.pyplot as plt
from fab_parser import parse
import os

samples_folder = os.getcwd().strip("code") + "gcode_samples"
data = parse(f"{samples_folder}/1_peca.gcode")

# COLOR NAMES: https://matplotlib.org/3.1.0/gallery/color/named_colors.html
colors = {
    "SUPPORT": "b", #blue
    "TRAVEL": "k", #black
    "SKIRT": "g", #green
    "WALL-OUTER": "r", #red
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
        for i, point in enumerate(line["Points"]):
            x.append(point[0])
            y.append(point[1])
            z.append(layer["z"])
            c += colors[line["Line Type"]]

for i in range(len(x)):
    ax.plot(x[i:i+2], y[i:i+2], z[i:i+2], color=c[i])

plt.show()

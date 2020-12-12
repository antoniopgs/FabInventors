import matplotlib.pyplot as plt

# COLOR NAMES: https://matplotlib.org/3.1.0/gallery/color/named_colors.html
colors = {
    "SUPPORT": "blue",
    "TRAVEL": "black",
    "SKIRT": "green",
    "WALL-OUTER": "red",
    "WALL-INNER": "cyan",
    "SKIN": "magenta",
    "FILL": "yellow",
}

def visualize(data):
    fig = plt.figure()
    ax = fig.gca(projection="3d")

    for layer in data["layers"].values():
        for line in layer["lines"]:
            for i, point in enumerate(line["Points"]):
                if i > 0:
                    prev_x, x = x, point[0]
                    prev_y, y = y, point[1]
                    prev_z, z = z, layer["z"]

                    ax.plot([prev_x, x], [prev_y, y], [prev_z, z], color=colors[line["Line Type"]])

                elif i == 0:
                    x = point[0]
                    y = point[1]
                    z = layer["z"]

    ax.legend(colors.keys(), labelcolor=colors.values())
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title(data["input"])
    plt.show()

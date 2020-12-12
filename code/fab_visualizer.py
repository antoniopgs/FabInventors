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
        try:
            prev_z, z = z, layer["z"]
        except UnboundLocalError:
            z = layer["z"]

        for i, line in enumerate(layer["lines"]):
            try:
                prev_x, x = x, line["Points"][0][0]
                prev_y, y = y, line["Points"][0][1]

                if i == 1:
                    prev_z = z
                    
                ax.plot([prev_x, x], [prev_y, y], [prev_z, z], color=colors[previous_line_type])

            except UnboundLocalError:
                x = line["Points"][0][0]
                y = line["Points"][0][1]

            previous_line_type = line["Line Type"]

    ax.legend(colors.keys(), labelcolor=colors.values())
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title(data["input"])
    plt.show()

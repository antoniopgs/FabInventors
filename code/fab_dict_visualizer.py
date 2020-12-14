import matplotlib.pyplot as plt

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

def visualize_dict(data):
    fig = plt.figure()
    ax = fig.gca(projection="3d")

    for layer in data["layers"].values():
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

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    ax.legend(colors.keys(), labelcolor=colors.values())
    ax.set_title(data["input"].replace(".gcode", " (JSON)"))
    
    return plt
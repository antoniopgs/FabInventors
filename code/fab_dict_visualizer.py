import matplotlib.pyplot as plt
from timer import timer

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

@timer
def visualize_dict(data):
    fig = plt.figure()
    ax = fig.gca(projection="3d")

    plot_data = []

    for line in data["lines"]:

        plot_data.append([
            (line["points"][0][0], line["points"][1][0]),
            (line["points"][0][1], line["points"][1][1]),
            (line["points"][0][2], line["points"][1][2]),
            colors[line["type"]]
        ])

        ax.plot(
            [line["points"][0][0], line["points"][1][0]],
            [line["points"][0][1], line["points"][1][1]],
            [line["points"][0][2], line["points"][1][2]],
            color=colors[line["type"]]
        )

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    ax.legend(colors.keys(), labelcolor=colors.values())
    ax.set_title(data["input"].replace(".gcode", " (JSON)"))
    
    return plot_data, fig

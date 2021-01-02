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
            (line["Points"][0][0], line["Points"][1][0]),
            (line["Points"][0][1], line["Points"][1][1]),
            (line["Points"][0][2], line["Points"][1][2]),
            colors[line["Line Type"]]
        ])

        ax.plot(
            [line["Points"][0][0], line["Points"][1][0]],
            [line["Points"][0][1], line["Points"][1][1]],
            [line["Points"][0][2], line["Points"][1][2]],
            color=colors[line["Line Type"]]
        )

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    ax.legend(colors.keys(), labelcolor=colors.values())
    ax.set_title(data["input"])
    
    return plot_data, fig

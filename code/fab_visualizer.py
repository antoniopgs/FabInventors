import matplotlib.pyplot as plt

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

def visualize(data):
    x, y, z = [], [], []
    c = ""
    
    for layer in data["layers"].values():
        for line in layer["lines"]:
            for point in line["Points"]:
                x.append(point[0])
                y.append(point[1])
                z.append(layer["z"])
                c += colors[line["Line Type"]]

    fig = plt.figure()
    ax = fig.gca(projection="3d")

    for i in range(len(x)):
        ax.plot(x[i:i+2], y[i:i+2], z[i:i+2], color=c[i])
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title(data["input"])
    plt.show()


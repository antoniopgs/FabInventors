import matplotlib.pyplot as plt

def visualize(data):
    x, y, z = [], [], []
    for layer in data["layers"].values():
        for line in layer["lines"]:
            for point in line["Points"]:
                x.append(point[0])
                y.append(point[1])
                z.append(layer["z"])

    fig = plt.figure()
    ax = fig.gca(projection="3d")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title(data["input"])
    ax.plot(x, y, z)
    plt.show()


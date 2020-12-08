import matplotlib.pyplot as plt
from fab_parser import parse
import json

def visualize(data):
    layers = json.loads(data)
    x, y, z = [], [], []

    for layer in layers.values():
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
    ax.plot(x, y, z)
    plt.show()


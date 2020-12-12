import matplotlib.pyplot as plt
import re, os

# COLOR NAMES: https://matplotlib.org/3.1.0/gallery/color/named_colors.html
colors = {
    "SETUP": "orange",
    "SUPPORT": "blue",
    "TRAVEL": "grey",
    "SKIRT": "green",
    "WALL-OUTER": "red",
    "WALL-INNER": "cyan",
    "SKIN": "magenta",
    "FILL": "black"
}

def visualize(file):
    fig = plt.figure()
    ax = fig.gca(projection="3d")

    for line in (x.strip("\n") for x in open(file)):
        if "G0 " in line or "G1 " in line:
            data = re.match("G[01]( F\d+\.?\d*)?( X\d+\.?\d*)?( Y\d+\.?\d*)?( Z-?\d+\.?\d*)?( E-?\d+\.?\d*)?", line)

            try:
                x = float(data.group(2).replace("X", ""))
            except AttributeError:
                x = prev_x

            try:
                y = float(data.group(3).replace("Y", ""))
            except AttributeError:
                y = prev_y

            try:
                z = float(data.group(4).replace("Z", ""))
            except AttributeError:
                z = prev_z
            
            if "G0 " in line:
                ax.plot([prev_x, x], [prev_y, y], [prev_z, z], color=colors["TRAVEL"])
            elif "G1 " in line:
                ax.plot([prev_x, x], [prev_y, y], [prev_z, z], color=colors[c])

            '''
            print(f"LINE: {line}")
            print(f"X: {prev_x} --> {x}")
            print(f"Y: {prev_y} --> {y}")
            print(f"Z: {prev_z} --> {z}")
            if "G0 " in line:
                print(f"C: TRAVEL")
            elif "G1 " in line:
                print(f"C: {c}")
            print()
            '''

            prev_x, prev_y, prev_z= x, y, z
        
        elif ";TYPE:" in line:
            c = re.match(";TYPE:(.*)", line).group(1)
        
        elif line == "G28 ;Home":
            prev_x, prev_y, prev_z, c = 0, 0, 0, "SETUP"

    ax.legend(colors.keys(), labelcolor=colors.values())
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    ax.set_xscale("linear")
    ax.set_yscale("linear")
    ax.set_zscale("linear")

    ax.set_title(os.path.basename(file))
    plt.show()

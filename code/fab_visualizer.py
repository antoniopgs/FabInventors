import matplotlib.pyplot as plt
import re, os

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

            if c == "SETUP":
                ax.plot([prev_x, x], [prev_y, y], [0.3, 0.3], color=colors["TRAVEL"])
            elif "G0 " in line:
                ax.plot([prev_x, x], [prev_y, y], [prev_z, z], color=colors["TRAVEL"])
            elif "G1 " in line:
                ax.plot([prev_x, x], [prev_y, y], [prev_z, z], color=colors[c])

            prev_x, prev_y, prev_z= x, y, z
        
        elif ";TYPE:" in line:
            c = re.match(";TYPE:(.*)", line).group(1)
        
        if line == "G28 ;Home":
            prev_x, prev_y, prev_z, c = 0, 0, 0, "SETUP"

    ax.legend(colors.keys(), labelcolor=colors.values())
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    ax.set_title(os.path.basename(file).replace(".gcode", " (G-Code)"))
    
    return plt

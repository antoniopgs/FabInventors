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
    start = False
    fig = plt.figure()
    ax = fig.gca(projection="3d")

    for line in (x.strip("\n") for x in open(file)):
        
        if start:
            
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

                prev_x, prev_y, prev_z= x, y, z
            
            elif ";TYPE:" in line:
                c = re.match(";TYPE:(.*)", line).group(1)
        
        elif ";LAYER_COUNT:" in line:
            start = True
            prev_x, prev_y, prev_z = 0, 0, 0.3 # No c because all lines between LAYER_COUNT & first TYPE are G0.

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    
    ax.legend(colors.keys(), labelcolor=colors.values())
    ax.set_title(os.path.basename(file).replace(".gcode", " (G-Code)"))

    return plt

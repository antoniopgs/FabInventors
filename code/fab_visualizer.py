import matplotlib.pyplot as plt
from timer import timer
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

@timer
def visualize(file):
    start = False
    fig = plt.figure()
    ax = fig.gca(projection="3d")
    plot_data = []
    prev_x, prev_y, prev_z = float(0), float(0), None # No c because all lines between LAYER_COUNT & first TYPE are G0.

    for line in (x.strip("\n") for x in open(file)):
        
        if start:
            
            if "G0 " in line or "G1 " in line:
                data = re.match("G[01]( F\d+\.?\d*)?( X\d+\.?\d*)?( Y\d+\.?\d*)?( Z-?\d+\.?\d*)?( E-?\d+\.?\d*)?", line)

                x = float(data.group(2).replace("X", "")) if data.group(2) else prev_x
                y = float(data.group(3).replace("Y", "")) if data.group(3) else prev_y
                z = float(data.group(4).replace("Z", "")) if data.group(4) else prev_z

                plot_data.append([(prev_x, x), (prev_y, y), (prev_z if prev_z else z, z), colors['TRAVEL'] if 'G0 ' in line else colors[c]])
                ax.plot([prev_x, x], [prev_y, y], [prev_z if prev_z else z, z], color = colors["TRAVEL"] if "G0 " in line else colors[c])

                prev_x, prev_y, prev_z = x, y, z
            
            elif ";TYPE:" in line:
                c = re.match(";TYPE:(.*)", line).group(1)
        
        elif ";LAYER_COUNT:" in line:
            start = True

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    
    ax.legend(colors.keys(), labelcolor=colors.values())
    ax.set_title(os.path.basename(file).replace(".gcode", " (G-Code)"))

    return plot_data, fig

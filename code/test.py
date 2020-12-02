from matplotlib import pyplot as plt
from fab_parser import parse
import os, json

samples_folder = os.getcwd().strip("code") + "gcode_samples"
colors_by_name = {
    "SUPPORT": "#0000ff",       #blue
    "NONMESH": "#00c951",       #green
    "TRAVEL": "#00c951",        #green
    "SKIRT": "#00c951",         #green
    "MESH_NAME": "#ff0000",     #red
    "WALL-OUTER": "#ff9a00",    #orange
    "WALL-INNER": "#ff9a00",    #orange
    "SKIN": "#d000ff",          #violet
    "FILL": "#fff700"           #yellow
}

def show_layer_from_json(layers, layer_key):
    if not layer_key in layers.keys():
        print("Layer nr.%s not exist" % layer_key)
        return

    layer = layers[layer_key]

    # Config figure
    fig = plt.figure(figsize=[8, 8])
    ax = fig.add_subplot(111)
    ax.axis('equal')
    ax.set_xlim([0, 200])
    ax.set_ylim([0, 200])
    plt.show(block=False)

    for line in layer["lines"]:
        points_x = [line["Points"][0][0], line["Points"][1][0]]
        points_y = [line["Points"][0][1], line["Points"][1][1]]
        ax.plot(points_x, points_y, color=colors_by_name[line["Line Type"]], linewidth=1)


if __name__ == "__main__":
    json_file = parse(f"{samples_folder}/1_peca.gcode")
    layers_dict = json.loads(json_file)
    show_layer_from_json(layers_dict, layer_key=str(10))

# For reference:
#
#     "G-Code Line Number": "i+1",
#     "G-Code Line": "data[i]",
#     "Part Name": "SUPPORT/MESH_NAME/NONMESH",
#     "Line type": "TRAVEL(se o ponto de destino == G0) / WALL-OUTER / WALL-INNER / SKIN / FILL / SUPPORT",
#     "Points": [("x1", "y1"), ("x2", "y2")],
#     "Extrusion length": ("E"),
#     "Speed": ("F")

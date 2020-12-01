import re, json

mesh = "NONMESH"
layers = {}

def get(group_number):
    try:
        return float(re.sub("[A-Z]", "", info.group(group_number)))
    except TypeError:
        if group_number == 5:
            return float(0)
        else:
            return get_previous(group_number)

def get_previous(group_number): # Get values from regex match.
    if group_number == 1:
        try:
            return layers[layer]["lines"][-1]["Speed"]
        except IndexError:
            return layers[layer - 1]["lines"][-1]["Speed"]
    elif group_number == 2:
        try:
            return layers[layer]["lines"][-1]["Points"][1][0]
        except IndexError:
            if layer == 0:
                return float(0)
            else:
                return layers[layer - 1]["lines"][-1]["Points"][1][0]
    elif group_number == 3:
        try:
            return layers[layer]["lines"][-1]["Points"][1][1]
        except IndexError:
            if layer == 0:
                return float(0)
            else:
                return layers[layer - 1]["lines"][-1]["Points"][1][1]
    elif group_number == 5:
        return float(0) # If nothing is extruded.

def check_travel(): # If line ends in a G0 Point, Line Type = TRAVEL.
    if "G0 " in movement:
        return "TRAVEL"
    
    elif "G1 " in movement:
        return line_type


for i, movement in enumerate(line.strip("\n") for line in open("gcode_samples/2_pecas_suporte.gcode")):

    if ";LAYER:" in movement:
        layer = int(re.match(";LAYER:(\d*)", movement).group(1))
        layers[layer] = {"z": None, "lines": []}

    elif 0 in layers: # If first layer was already found.
        if "G0 " in movement or "G1 " in movement:
            info = re.match("G[01]( F\d+\.?\d*)?( X\d+\.?\d*)?( Y\d+\.?\d*)?( Z-?\d+\.?\d*)?( E-?\d+\.?\d*)?", movement)
            layers[layer]["lines"].append({
                "G-Code Line Number": i + 1, # i is only incremented after the first two lines.
                "G-Code Line": movement,
                "Part Name": mesh,
                "Line Type": check_travel(),
                "Points": [
                    (get_previous(2), get_previous(3)),
                    (get(2), get(3))
                ],
                "Extrusion Length": get(5),
                "Speed": get(1)
            })

            if info.group(4): # If Z exists.
                if not layers[0]["z"]: # Layer 0 has 2 z values. First one is for layer 0.
                    layers[0]["z"] = get(4)
                else: # Layer 0's second z value, and all further z values are for the next layer (layer + 1).
                    layers[layer + 1] = {"z": get(4)}

        elif ";TYPE:" in movement:
            line_type = re.match(";TYPE:(.*)", movement).group(1)

        elif ";MESH:" in movement:
            mesh = re.match(";MESH:(.*)", movement).group(1)

output = json.dumps(layers, indent=4)
print(output)

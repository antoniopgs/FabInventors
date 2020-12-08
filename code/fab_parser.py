import json, re, os

data = {}

def get(layer_value, data, group_number):
    try:
        return float(re.sub("[A-Z]", "", data.group(group_number)))
    except TypeError:
        if group_number == 5:
            return float(0)
        else:
            return get_previous(layer_value, group_number)

def get_previous(layer_value, group_number): # Get values from regex match.
    if group_number == 1:
        try:
            return data["layers"][layer_value]["lines"][-1]["Speed"]
        except IndexError:
            return data["layers"][layer_value - 1]["lines"][-1]["Speed"]
    elif group_number == 2:
        try:
            return data["layers"][layer_value]["lines"][-1]["Points"][1][0]
        except IndexError:
            if layer_value == 0:
                return float(0)
            else:
                return data["layers"][layer_value - 1]["lines"][-1]["Points"][1][0]
    elif group_number == 3:
        try:
            return data["layers"][layer_value]["lines"][-1]["Points"][1][1]
        except IndexError:
            if layer_value == 0:
                return float(0)
            else:
                return data["layers"][layer_value - 1]["lines"][-1]["Points"][1][1]
    elif group_number == 5:
        return float(0) # If nothing is extruded.

def check_travel(line, return_value): # If line ends in a G0 Point, Line Type = TRAVEL.
    if "G0 " in line:
        return "TRAVEL"
    elif "G1 " in line:
        return return_value

def parse(file):
    data["input"] = os.path.basename(file)
    start = False
    mesh = "NONMESH"
    line_type = None

    for i, movement in enumerate(line.strip("\n") for line in open(file)):

        if start:
            
            if "G0 " in movement or "G1 " in movement:
                info = re.match("G[01]( F\d+\.?\d*)?( X\d+\.?\d*)?( Y\d+\.?\d*)?( Z-?\d+\.?\d*)?( E-?\d+\.?\d*)?", movement)
                
                if info.group(4): # If Z exists.
                    if "layers" not in data:
                        data["layers"] = {0: {"z": get(layer, info, 4), "lines": []}}
                    else:
                        data["layers"][layer + 1] = {"z": get(layer, info, 4), "lines": []}

                data["layers"][layer]["lines"].append({
                    "G-Code Line Number": i + 1, # i is only incremented after the first two lines.
                    "G-Code Line": movement,
                    "Part Name": mesh,
                    "Line Type": check_travel(movement, line_type),
                    "Points": [
                        (get_previous(layer, 2), get_previous(layer, 3)),
                        (get(layer, info, 2), get(layer, info, 3))
                    ],
                    "Extrusion Length": get(layer, info, 5),
                    "Speed": get(layer, info, 1)
                })

            elif ";TYPE:" in movement:
                line_type = re.match(";TYPE:(.*)", movement).group(1)

            elif ";MESH:" in movement:
                mesh = re.match(";MESH:(.*)", movement).group(1)

            elif ";LAYER:" in movement:
                layer = int(re.match(";LAYER:(.*)", movement).group(1))
        
        
        elif ";LAYER_COUNT:" in movement:
            start = True

    return json.dumps(data, indent=4)

import re, json

start = False
layer = 0
previous_speed = 0
previous_x, previous_y = 0, 0 # First Line of First Layer of First Part starts at x = 0, y = 0 (home).
mesh = None # If no mesh in file, mesh = None.

def get(a): # Get values from regex match.
    if a == "speed":
        try:
            return float(info.group(1).strip().strip("F"))
        except AttributeError:
            return previous_speed
    elif a == "x":
        try:
            return float(info.group(2).strip().strip("X"))
        except AttributeError:
            return previous_x
    elif a == "y":
        try:
            return float(info.group(3).strip().strip("Y"))
        except AttributeError:
            return previous_y
    elif a == "extrusion":
        try:
            return float(info.group(5).strip().strip("E"))
        except AttributeError:
            return float(0) # If nothing is extruded.

def travel(): # If line ends in a G0 Point, Line Type = TRAVEL.
    if "G0 " in data[i]:
        return "TRAVEL"
    
    else:
        return current_type
            

with open("gcode_samples/2_pecas_suporte.gcode") as file:
    data = [movement.strip("\n") for movement in file.readlines()]
    for x in data:
        if ";MESH:" in x:
            mesh = "NONMESH" # If any mesh in file, everything before mesh is NONMESH.
            break

for i in range(len(data)):

    if not start:
        if ";LAYER_COUNT:" in data[i]:
            layer_count = int(re.match(";LAYER_COUNT:(\d*)", data[i]).group(1))
            layers = {}
            for n in range(layer_count):
                layers[n] = {"z": None,
                             "lines": []}
            start = True
        
    else:
        if "G0 " in data[i] or "G1 " in data[i]:
            info = re.match("G[01]( F\d+\.?\d*)?( X\d+\.?\d*)?( Y\d+\.?\d*)?( Z-?\d+\.?\d*)?( E-?\d+\.?\d*)?", data[i])
            speed, x, y, extrusion = get("speed"), get("x"), get("y"), get("extrusion")
            if extrusion == float(0): # Only worth it to check for z when there is no extrusion.
                if info.group(4): # If z has a value, which means z is not None.
                    if not layers[0]["z"]: # Layer 0 has 2 z values. First one is for layer 0.
                        layers[0]["z"] = float(info.group(4).strip().strip("Z")) # 
                    else: # Layer 0's second z value, and all further z values are for the next layer.
                        layers[layer + 1]["z"] = float(info.group(4).strip().strip("Z")) # Z is attributed to the upcoming layer (layer + 1).
            line = {"G-Code Line Number": i+1,
                    "G-Code Line": data[i],
                    "Part Name": mesh,
                    "Line Type": travel(),
                    "Points": [(previous_x, previous_y), (x, y)],
                    "Extrusion Length": extrusion,
                    "Speed": speed
                    }
            layers[layer]["lines"].append(line)
            previous_x, previous_y, previous_speed = x, y, speed # Update previous values to current values.

        elif ";TYPE:" in data[i]:
            current_type = re.match(";TYPE:(.*)", data[i]).group(1)

        elif ";LAYER:" in data[i]:
            layer = int(re.match(";LAYER:(\d*)", data[i]).group(1))
            continue

        elif ";MESH:" in data[i]:
            mesh = re.match(";MESH:(.*)", data[i]).group(1)
            

output = json.dumps(layers, indent=4)
print(output)

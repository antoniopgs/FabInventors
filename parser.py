import re, json

start = False
layer = 0
previous_speed = 0
previous_x, previous_y = 0, 0 # First Line of First Layer of First Part starts at x = 0, y = 0 (home).
mesh = None # If no mesh in file, mesh = None.

def get(group_number): # Get values from regex match.
    try:
        return float(re.sub("[A-Z]", "", info.group(group_number)))
    except TypeError:
        if group_number == 1:
            return previous_speed
        elif group_number == 2:
            return previous_x
        elif group_number == 3:
            return previous_y
        elif group_number == 5:
            return float(0) # If nothing is extruded.

def check_travel(): # If line ends in a G0 Point, Line Type = TRAVEL.
    if "G0 " in pair[1]:
        return "TRAVEL"
    
    elif "G1 " in pair[1]:
        return current_type

def gen_line_pairs(file):
    iterator = iter(open(file))
    previous_line = next(iterator)
    for line in iterator:
        yield previous_line.strip("\n"), line.strip("\n")
        previous_line = line
        
for x in [movement.strip("\n") for movement in open("gcode_samples/2_pecas_suporte.gcode").readlines()]:
    if ";MESH:" in x:
        mesh = "NONMESH" # If any mesh in file, everything before mesh is NONMESH.
        break

for pair in gen_line_pairs("gcode_samples/2_pecas_suporte.gcode"):

    if not start:
        try:
            layer_count = int(re.match(";LAYER_COUNT:(\d*)", pair[1]).group(1))
            layers = {}
            for n in range(layer_count):
                layers[n] = {"z": None,
                             "lines": []}
            start = True
        except:
            continue
        
    else:
        if "G0 " in pair[1] or "G1 " in pair[1]:
            info = re.match("G[01]( F\d+\.?\d*)?( X\d+\.?\d*)?( Y\d+\.?\d*)?( Z-?\d+\.?\d*)?( E-?\d+\.?\d*)?", pair[1])
            speed, x, y, extrusion = get(1), get(2), get(3), get(5)
            if extrusion == float(0): # Only worth it to check for z when there is no extrusion.
                if info.group(4): # If z has a value, which means z is not None.
                    if not layers[0]["z"]: # Layer 0 has 2 z values. First one is for layer 0.
                        layers[0]["z"] = get(4)
                    else: # Layer 0's second z value, and all further z values are for the next layer.
                        layers[layer + 1]["z"] = get(4) # Z is attributed to the upcoming layer (layer + 1).
            line = {"G-Code Line Number": "???",
                    "G-Code Line": pair[1],
                    "Part Name": mesh,
                    "Line Type": check_travel(),
                    "Points": [(previous_x, previous_y), (x, y)],
                    "Extrusion Length": extrusion,
                    "Speed": speed
                    }
            layers[layer]["lines"].append(line)
            previous_x, previous_y, previous_speed = x, y, speed # Update previous values to current values.

        elif ";TYPE:" in pair[1]:
            current_type = re.match(";TYPE:(.*)", pair[1]).group(1)

        elif ";LAYER:" in pair[1]:
            layer = int(re.match(";LAYER:(\d*)", pair[1]).group(1))

        elif ";MESH:" in pair[1]:
            mesh = re.match(";MESH:(.*)", pair[1]).group(1)
            

output = json.dumps(layers, indent=4)
print(output)

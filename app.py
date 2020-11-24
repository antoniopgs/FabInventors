import re, json

parts = {}
start = False
layer = 0
previous_speed = 0
previous_x, previous_y = 0, 0 # First Line of First Layer of First Piece starts at x = 0, y = 0 (home)
current_type = "TRAVEL"

def get(a): # Get values from regex match
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
            return float(info.group(4).strip().strip("E"))
        except AttributeError:
            return float(0) # if nothing is extruded
            

with open("gcode_samples/1_peca_suporte.gcode") as file:
    data = [movement.strip("\n") for movement in file.readlines()]

for i in range(len(data)):

    if not start:
        if ";LAYER_COUNT:" in data[i]:
            layer_count = int(re.match(";LAYER_COUNT:(\d*)", data[i]).group(1))
            layers = {}
            for n in range(layer_count):
                layers[n] = []
            start = True
        
    else:
        if re.match(";LAYER:\d*", data[i]):
            layer = int(re.match(";LAYER:(\d*)", data[i]).group(1))
            continue

        elif ";TYPE:" in data[i]:
            current_type = re.match(";TYPE:(.*)", data[i]).group(1)

        elif re.match("G[01]( F\d+\.?\d*)?( X\d+\.?\d*)?( Y\d+\.?\d*)?( E-?\d+\.?\d*)?", data[i]):
            info = re.match("G[01]( F\d+\.?\d*)?( X\d+\.?\d*)?( Y\d+\.?\d*)?( E-?\d+\.?\d*)?", data[i])
            speed, x, y, extrusion = get("speed"), get("x"), get("y"), get("extrusion")
            line = {"G-Code Line": i+1,
                    "Line type": current_type,
                    "Points": [(previous_x, previous_y), (x, y)],
                    "Extrusion Length": extrusion,
                    "Speed": speed
                    }
            layers[layer].append(line)
            previous_x, previous_y, previous_speed = x, y, speed # Update previous values to current values

output = json.dumps(layers, indent=4)
print(output)

import re
import json

parts = {}
start = False
current_layer = 0


with open("gcode_samples/1_peca_suporte.gcode") as file:
    data = [movement.strip("\n") for movement in file.readlines()]

previous_x, previous_y, previous_speed = 0, 0, 0
current_type = "TRAVEL"
for i in range(len(data)):

    if ";LAYER_COUNT:" in data[i]:
        layer_count = int(re.match("^;LAYER_COUNT:(\d*)", data[i]).group(1))
        layers = {}
        for n in range(layer_count):
            layers[n] = []
        start = True
        
    if start:

        if re.match("^;LAYER:\d*", data[i]):
            current_layer = int(re.match("^;LAYER:(\d*)", data[i]).group(1))
            continue

        elif ";TYPE:" in data[i]:
            current_type = re.match("^;TYPE:(.*)", data[i]).group(1)

        elif re.match("^G[01] (F\d+\.?\d*)? (X\d+\.?\d*)? (Y\d+\.?\d*)? (E-?\d+\.?\d*)?", data[i]):
            info = re.match("^G[01] (F\d+\.?\d*)? (X\d+\.?\d*)? (Y\d+\.?\d*)? (E-?\d+\.?\d*)?", data[i])
            try:
                extrusion = float(info.group(4).strip("E"))
            except AttributeError:
                extrusion = float(0)
            try:
                speed = float(info.group(1).strip("F"))
            except AttributeError:
                speed = previous_speed
            try:
                current_x = float(info.group(2).strip("X"))
            except AttributeError:
                current_x = previous_x
            try:
                current_y = float(info.group(3).strip("Y"))
            except AttributeError:
                current_y = previous_y
                
            line = {"Current Line": i+1,
                    "Line type": current_type,
                    "Points": [(previous_x, previous_y), (current_x, current_y)],
                    "Extrusion Length": extrusion,
                    "Speed": speed
                    }
            layers[current_layer].append(line)
            previous_x = current_x
            previous_y = current_y
            previous_speed = speed

output = json.dumps(layers, indent=4)
print(output)

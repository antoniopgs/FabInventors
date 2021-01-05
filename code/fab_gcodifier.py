import os

def gcodify(json_data):
    if not os.path.exists("./new-gcodes"):
        os.makedirs("./new-gcodes")

    with open(f"./new-gcodes/{json_data['input']}", "w") as output: # Mode is 'w' to overwrite file if it already exists.
        
        output.write(";LAYER_COUNT:\n") # Parser needs this line to start.

        previous_line_type = None
        previous_mesh = None
        
        for line in json_data["lines"]:

            points = line["points"][1]
            x, y, z = points[0], points[1], points[2]
            f, e = line["speed"], line["extrusion"]
            line_type, mesh = line["type"], line["mesh"]

            if line_type != previous_line_type:
                output.write(f";TYPE:{line_type}\n")

            if mesh != previous_mesh:
                output.write(f";MESH:{mesh}\n")

            if not e and line_type == "TRAVEL":
                mov_type = "0"
            else:
                mov_type = "1"

            gcode_line = f"G{mov_type} F{f} X{x} Y{y} Z{z}"

            if e:
                gcode_line += f" E{e}"

            output.write(f"{gcode_line}\n")

            previous_mesh, previous_line_type = mesh, line_type

    return output
            
            
            
        

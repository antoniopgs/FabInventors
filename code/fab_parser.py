import re, os

def parse(file):
    start = False
    data = {"input": os.path.basename(file), "lines": []}
    prev_x, prev_y, prev_z = float(0), float(0), None # Always start at home (0, 0).
    line_type = None
    mesh = "NONMESH"

    for line in (x.strip("\n") for x in open(file)):

        if start:
            
            if "G0 " in line or "G1 " in line:
                info = re.match("G[01]( F\d+\.?\d*)?( X\d+\.?\d*)?( Y\d+\.?\d*)?( Z-?\d+\.?\d*)?( E-?\d+\.?\d*)?", line)

                speed = float(info.group(1).replace("F", "")) if info.group(1) else prev_speed
                x = float(info.group(2).replace("X", "")) if info.group(2) else prev_x
                y = float(info.group(3).replace("Y", "")) if info.group(3) else prev_y
                z = float(info.group(4).replace("Z", "")) if info.group(4) else prev_z
                extrusion = float(info.group(5).replace("E", "")) if info.group(5) else float(0) # No apparent "previous extrusion" values. It's always explicit.

                data["lines"].append({
                    "points": [
                        (prev_x, prev_y, prev_z if prev_z else z),
                        (x, y, z)
                    ],
                    "speed": speed,
                    "extrusion": extrusion,
                    "type": "TRAVEL" if "G0 " in line else line_type,
                    "mesh": mesh
                })

                prev_speed, prev_x, prev_y, prev_z, prev_extrusion = speed, x, y, z, extrusion

            elif ";TYPE:" in line:
                line_type = re.match(";TYPE:(.*)", line).group(1)

            elif ";MESH:" in line:
                mesh = re.match(";MESH:(.*)", line).group(1)
        
        elif ";LAYER_COUNT:" in line:
            start = True

    return data

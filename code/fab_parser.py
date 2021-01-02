import re, os

data = {}

def parse(file):
    start = False
    data["input"] = os.path.basename(file)
    data["lines"] = []
    mesh = "NONMESH"
    line_type = None
    prev_x, prev_y, prev_z = float(0), float(0), None

    for i, movement in enumerate(line.strip("\n") for line in open(file)):

        if start:
            
            if "G0 " in movement or "G1 " in movement:
                info = re.match("G[01]( F\d+\.?\d*)?( X\d+\.?\d*)?( Y\d+\.?\d*)?( Z-?\d+\.?\d*)?( E-?\d+\.?\d*)?", movement)

                speed = float(info.group(1).replace("F", "")) if info.group(1) else prev_speed
                x = float(info.group(2).replace("X", "")) if info.group(2) else prev_x
                y = float(info.group(3).replace("Y", "")) if info.group(3) else prev_y
                z = float(info.group(4).replace("Z", "")) if info.group(4) else prev_z
                extrusion = float(info.group(5).replace("E", "")) if info.group(5) else None # No apparent "previous extrusion" values. It's always explicit.

                data["lines"].append({
                    "line_number": i + 1, # i is only incremented after the first two lines.
                    "line_content": movement,
                    "part": mesh,
                    "type": "TRAVEL" if "G0 " in movement else line_type,
                    "points": [
                        (prev_x, prev_y, prev_z if prev_z else z),
                        (x, y, z)
                    ],
                    "extrusion": extrusion,
                    "speed": speed
                })

                prev_speed = speed
                prev_x = x
                prev_y = y
                prev_z = z
                prev_extrusion = extrusion

            elif ";TYPE:" in movement:
                line_type = re.match(";TYPE:(.*)", movement).group(1)

            elif ";MESH:" in movement:
                mesh = re.match(";MESH:(.*)", movement).group(1)
        
        elif ";LAYER_COUNT:" in movement:
            start = True

    return data

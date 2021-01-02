data = {
    "input": "xyz.gcode",
    "lines": [
        {"line_number": "i+1",
        "line_content": "data[i]",
        "part": "MESH_NAME/NONMESH",
        "type": "TRAVEL(if 'G0' in line_content) / WALL-OUTER / WALL-INNER / SKIN / FILL / SUPPORT / SKIRT",
        "points": [("x1", "y1", "z1"), ("x2", "y2", "z2")], # Milimeters
        "extrusion": "E", # Milimeters
        "speed": "F" # Milimeters per Minute
        },
        {"line_number": "i+1",
        "line_content": "data[i]",
        "part": "MESH_NAME/NONMESH",
        "type": "TRAVEL(if 'G0' in line_content) / WALL-OUTER / WALL-INNER / SKIN / FILL / SUPPORT / SKIRT",
        "points": [("x1", "y1", "z1"), ("x2", "y2", "z2")], # Milimeters
        "extrusion": "E", # Milimeters
        "speed": "F" # Milimeters per Minute
        },
        {"line_number": "i+1",
        "line_content": "data[i]",
        "part": "MESH_NAME/NONMESH",
        "type": "TRAVEL(if 'G0' in line_content) / WALL-OUTER / WALL-INNER / SKIN / FILL / SUPPORT / SKIRT",
        "points": [("x1", "y1", "z1"), ("x2", "y2", "z2")], # Milimeters
        "extrusion": "E", # Milimeters
        "speed": "F" # Milimeters per Minute
        },
    ]
},

# Só a peça de Suporte tem ID = 0. Caso não haja peça de suporte, os IDs de peça começam em 1.
# A 1ª linha da primeira camada da primeira peça, começa em home (0, 0) e acaba no 1º ponto (o 1º ponto a seguir a "Layer Count")

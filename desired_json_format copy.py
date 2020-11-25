layers = {
    0: {"z": "z_value",
        "lines": [
            {"G-Code Line Number": "i+1",
            "G-Code Line": "data[i]",
            "Part Name": "SUPPORT/MESH_NAME/NONMESH",
            "Line type": "TRAVEL(se o ponto de destino == G0) / WALL-OUTER / WALL-INNER / SKIN / FILL / SUPPORT",
            "Points": [("x1","y1"), ("x2","y2")],
            "Extrusion length": ("E"),
            "Speed": ("F")
            },
            {"G-Code Line Number": "i+1",
            "G-Code Line": "data[i]",
            "Part Name": "SUPPORT/MESH_NAME/NONMESH",
            "Line type": "TRAVEL(se o ponto de destino == G0) / WALL-OUTER / WALL-INNER / SKIN / FILL / SUPPORT",
            "Points": [("x1","y1"), ("x2","y2")],
            "Extrusion length": ("E"),
            "Speed": ("F")
            }
        ],
    }
}

# Só a peça de Suporte tem ID = 0. Caso não haja peça de suporte, os IDs de peça começam em 1.
# A 1ª linha da primeira camada da primeira peça, começa em home (0, 0) e acaba no 1º ponto (o 1º ponto a seguir a "Layer Count")

# FabInventors
Software to facilitate multi-head 3D Printer control, provide print time duration estimates, and calculate energy and material consumption.

## Intro
3D Printers need input instructions on how to fabricate a given part.

These instructions are usually provided in a file format called G-Code.

A G-Code file is basically a series of points (along with speed, extrusion and some other properties)

A sample of G-Code can be seen here:

![image](https://user-images.githubusercontent.com/44982443/126477537-bc3d478d-57d9-4aa1-b248-3eb14c4c55a9.png)

**Description:**
- G1 = Line with material extrusion
- G0 = Line without material extrusion (travel line)
- F = Print Head Speed
- X = X coordinate
- Y = Y coordinate
- Z = Z coordinate (not shown here - 3D parts are printed layer by layer, so z changes happen with less frequency)
- E = Amount of material extruded


## Problem to Solve
To reduce the manufacturing time, FabInventors is developing a Multi-Head 3D Printer.

In order to properly provide G-Code instructions to this Multi-Head 3D Printer, they would have to be sliced, according to the spatial distribution of the various print heads.

However, in order to slice G-Code instructions, one needs to calculate intersections.

And in order to calculate intersections, one needs lines. But G-Code instructions consist of a series of points.

## Goal
**Therefore, this software intends to:**
1. Receive a G-Code input
2. Parse it from a series of points, to a series of lines
3. Slice said series of lines (with a dynamic number of rows and columns, to accommodate any table distribution of print-heads) into multiple files.
4. Convert each slice file back into a the G-Code format
5. Feed the G-Code file of each slice into each head of the Multi-Head 3D Printer.

**This flow can also be seen here:**

![Flowchart](https://user-images.githubusercontent.com/44982443/126475040-a6300796-e47e-4e2e-ba59-951f878dd00e.png)

(higher quality version here: [Flowchart.pdf](https://github.com/antoniopgs/FabInventors/files/6854870/Flowchart.pdf))

### Desired JSON Format
The G-Code files should be parsed into a JSON with the following format:
```
data = {
    "input": "xyz.gcode",
    "lines": [
        {"points": [(0, 0, "z2"), ("x2", "y2", "z2")], # Milimeters
        "speed": "F", # Milimeters per Minute
        "extrusion": "E", # Milimeters
        "type": "TRAVEL(if 'G0' in line_content) / WALL-OUTER / WALL-INNER / SKIN / FILL / SUPPORT / SKIRT",
        "mesh": "MESH_NAME/NONMESH"
        },
        {"points": [("x1", "y1", "z1"), ("x2", "y2", "z2")], # Milimeters
        "speed": "F", # Milimeters per Minute
        "extrusion": "E", # Milimeters
        "type": "TRAVEL(if 'G0' in line_content) / WALL-OUTER / WALL-INNER / SKIN / FILL / SUPPORT / SKIRT",
        "mesh": "MESH_NAME/NONMESH"
        },
        {"points": [("x1", "y1", "z1"), ("x2", "y2", "z2")], # Milimeters
        "speed": "F", # Milimeters per Minute
        "extrusion": "E", # Milimeters
        "type": "TRAVEL(if 'G0' in line_content) / WALL-OUTER / WALL-INNER / SKIN / FILL / SUPPORT / SKIRT",
        "mesh": "MESH_NAME/NONMESH"
        },
    ]
}
```

### Extras
**The software will also feature:**
- A series of estimators for print-time duration, energy consumption and material expenditure. _(IN PROGRESS)_
- A fully-adjustable 3D Visualizer, complete with color features and able to project both complete parts and slices.

#### Estimator Physics
**The estimators will perform calculations on several physical factors like:**
- motor strength
- material weight
- print head acceleration
- etc

#### Visualizer
**The 3D Visualizer can be seen here:**

![image](https://user-images.githubusercontent.com/44982443/126475410-b73347ac-e330-43b9-82eb-c4a2236c35f5.png)

#### Potential Improvements
- Implement tests, to see if all final products match the Original G-Code products.
- Once all tests are passed, implement some CI (maybe with GitHub Actions) to automatically run all tests whenever new code is pushed to master, to ensure quality and guarantee that no new code compromises product integrity.

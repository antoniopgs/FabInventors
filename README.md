# FabInventors
Software to facilitate multi-head 3D Printer control, provide print time duration estimates, and calculate energy and material consumption.

## Intro
3D Printers need input instructions on how to fabricate a given part.

These instructions are usually provided in a file format called G-Code.

A sample of G-Code can be seen here:

## Problem to Solve
To reduce the manufacturing time, FabInventors is developing a Multi-Head 3D Printer.

In order to properly provide G-Code instructions to this Multi-Head 3D Printer, they would have to be sliced, according to the spatial distribution of the various print heads.

However, in order to slice G-Code instructions, one needs to calculate intersections.

And in order to calculate intersections, one needs lines. But G-Code instructions consist of a series of points.

## Goal
Therefore, this software intends to:
1. Receive a G-Code input
2. Parse it from a series of points, to a series of lines
3. Slice said series of lines (with a dynamic number of rows and columns, to accommodate any table distribution of print-heads) into multiple files.
4. Convert each slice file back into a the G-Code format
5. Feed the G-Code file of each slice into each head of the Multi-Head 3D Printer.

This flow can be seen here:
![image](https://user-images.githubusercontent.com/44982443/126473210-09949b1a-f742-40b5-9e13-9b0ca40d3c4e.png)

### Extras
The software will also feature:
- A fully-adjustable 3D Visualizer, complete with color features and able to project both complete parts and slices.
- A series of estimators for print-time duration, energy consumption and material expenditure. **(IN PROGRESS)**
- Multi-Threading, to increase processing speed. **(IN PROGRESS)**

The 3D Visualizer can be seen here:


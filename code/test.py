from fab_visualizer import visualize
from fab_estimator import estimate
from fab_gcodifier import gcodify
from fab_slicer import slice_json
from fab_parser import parse

samples_folder = "./../gcode_samples/"
gcode_file = samples_folder + "1_peca.gcode"

file_json = parse(gcode_file)

slices = slice_json(file_json, rows=2, columns=1)

chosen_slice = slices["slice-2"]

slice_gcode = gcodify(chosen_slice)

slice_json = parse(f"./new-gcodes/{chosen_slice['input']}")

slice_fig = visualize(slice_json)
slice_fig.show()


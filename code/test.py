from fab_visualizer import visualize
from fab_estimator import estimate
from fab_gcodifier import gcodify
from fab_slicer import slice_json
from fab_parser import parse
import json

samples_folder = "./../gcode_samples/"
gcode_file = samples_folder + "1_peca.gcode"

json_data = parse(gcode_file)

slices = slice_json(json_data)
chosen_slice = slices["slice-1"]
gcodify(chosen_slice)

slice_file = chosen_slice["input"]
slice_data = parse(slice_file)

slice_fig = visualize(slice_data)
slice_fig.show()

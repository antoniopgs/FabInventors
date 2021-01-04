from fab_visualizer import visualize
from fab_estimator import estimate
from fab_gcodifier import gcodify
from fab_slicer import slice_json
from fab_parser import parse

samples_folder = "./../gcode_samples/"
gcode_file = samples_folder + "2_pecas.gcode"

json_data = parse(gcode_file)

slices = slice_json(json_data, rows=2, columns=3)

chosen_slice = slices["slice-3"]
gcodify(chosen_slice)

slice_file = chosen_slice["input"]
slice_data = parse(slice_file)

slice_fig = visualize(slice_data)
slice_fig.show()

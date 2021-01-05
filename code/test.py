from fab_visualizer import visualize
from fab_estimator import estimate
from fab_gcodifier import gcodify
from fab_slicer import slice_json
from fab_parser import parse

samples_folder = "./../gcode_samples/"
gcode_file = samples_folder + "1_peca.gcode"

file_json = parse(gcode_file)

main_fig = visualize(file_json)
main_fig.show()

slices = slice_json(file_json, rows=2, columns=3)

chosen_slice = slices["slice-3"]

slice_fig = visualize(chosen_slice)
slice_fig.show()

slice_gcode = gcodify(chosen_slice)

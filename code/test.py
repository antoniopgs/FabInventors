from fab_parser import parse
from fab_visualizer import visualize
from fab_slicer import slice_json
from fab_gcodifier import gcodify

samples_folder = "./../gcode_samples/"
gcode_file = samples_folder + "1_peca.gcode"

file_json = parse(gcode_file)

main_fig = visualize(file_json)
main_fig.show()

slices = slice_json(file_json, rows=2, columns=1)

chosen_slice = slices["slice-2"]

slice_fig = visualize(chosen_slice)
slice_fig.show()

slice_gcode = gcodify(chosen_slice)

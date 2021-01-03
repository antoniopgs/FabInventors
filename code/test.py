from fab_visualizer import visualize
from fab_estimator import estimate
from fab_slicer import slice_json
from fab_parser import parse
import json

samples_folder = "./../gcode_samples/"
gcode_file = samples_folder + "1_peca.gcode"

json_data = parse(gcode_file)
main_fig = visualize(json_data)
main_fig.show()

slices = slice_json(json_data)
for key in slices:
    temp_fig = visualize(slices[key])
    temp_fig.show()

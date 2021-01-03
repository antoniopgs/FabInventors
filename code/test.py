from fab_visualizer import visualize
from fab_estimator import estimate
from fab_slicer import slice_json
from fab_parser import parse

samples_folder = "./../gcode_samples/"
g_code = samples_folder + "1_peca.gcode"

json = parse(g_code)
fig_1 = slice_json(json)
fig_1.show()

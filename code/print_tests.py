from fab_gcodifier import gcodify
from fab_slicer import slice_json
from fab_parser import parse

samples_folder = "./../gcode_samples/"
gcode_file = samples_folder + "1_peca_suporte.gcode"

json_data = parse(gcode_file)

slices = slice_json(json_data, slices=3)

chosen_slice = slices["slice-1"]
gcodify(chosen_slice)


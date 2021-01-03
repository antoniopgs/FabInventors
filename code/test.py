from fab_visualizer import visualize
from fab_estimator import estimate
from fab_gcodifier import gcodify
from fab_slicer import slice_json
from fab_parser import parse

samples_folder = "./../gcode_samples/"
gcode_file = samples_folder + "1_peca.gcode"

json_data = parse(gcode_file)

main_fig = visualize(json_data)
main_fig.show()

slices = slice_json(json_data, slices=2)
chosen_slice = slices["slice-1"]
gcodify(chosen_slice)

slice_file = chosen_slice["input"]
slice_data = parse(slice_file)

slice_estimation = estimate(slice_data)
print(f"{slice_file} print time estimation: {slice_estimation}s") # Estimations are weird.

slice_fig = visualize(slice_data)
slice_fig.show() # Skirts are weird.

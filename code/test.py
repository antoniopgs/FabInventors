from fab_parser import parse
import os

sample_folder = os.getcwd().strip("code") + "gcode_samples\\"

json = parse(f"{sample_folder}/1_peca.gcode")
print(json)

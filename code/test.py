from fab_dict_visualizer import visualize_dict
from fab_visualizer import visualize
from fab_estimator import estimate
from fab_parser import parse
import os, json

samples_folder = os.getcwd().strip("code") + "gcode_samples"

for sample in os.listdir(samples_folder):
    #print(f"Sample: {sample}\nPrint Time: {estimate(data)}\n")
    p1 = visualize_dict(parse(f"{samples_folder}/{sample}"))
    p2 = visualize(f"{samples_folder}/{sample}")
    p1.show()
    p2.show()

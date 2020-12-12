from fab_dict_visualizer import visualize_dict
from fab_visualizer import visualize
from fab_estimator import estimate
from fab_parser import parse
import os, json

samples_folder = os.getcwd().strip("code") + "gcode_samples"

for sample in os.listdir(samples_folder):
    data = parse(f"{samples_folder}/{sample}")
    #print(f"Sample: {sample}\nPrint Time: {estimate(data)}\n")
    visualize_dict(data)
    #visualize(f"{samples_folder}/{sample}")

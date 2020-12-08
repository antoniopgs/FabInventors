from fab_visualizer import visualize
from fab_estimator import estimate
from fab_parser import parse
import os

samples_folder = os.getcwd().strip("code") + "gcode_samples"
samples = os.listdir(samples_folder)

for sample in samples:
    json = parse(f"{samples_folder}/{sample}")
    print(f"Sample: {sample}\nPrint Time: {estimate(json)}\n")
    visualize(json)

from fab_visualizer import visualize
from fab_estimator import estimate
from fab_parser import parse
import os

samples_folder = os.getcwd().strip("code") + "gcode_samples"

for sample in os.listdir(samples_folder):
    data = parse(f"{samples_folder}/{sample}")
    print(f"Sample: {sample}\nPrint Time: {estimate(data)}\n")
    visualize(data)

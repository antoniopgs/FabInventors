from fab_dict_visualizer import visualize_dict
from fab_visualizer import visualize
from fab_estimator import estimate
from fab_parser import parse
import os, json

samples_folder = os.getcwd().strip("code") + "gcode_samples"

file = os.listdir(samples_folder)[2]
#print(json.dumps(data, indent=4))
#break
#estimation = estimate(data)
#print(f"Sample: {sample}\nPrint Time: {estimation}\n")
p1 = visualize_dict(parse(f"{samples_folder}/{file}"))
p2 = visualize(f"{samples_folder}/{file}")
p1.show()
p2.show()

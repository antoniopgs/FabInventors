import math, os, json
from fab_parser import parse

def estimate(file):
    samples_folder = os.getcwd().strip("code") + "gcode_samples"
    time = 0
    for layer in (x for x in json.loads(parse(f"{samples_folder}/{file}")).values()):
        for line in layer["lines"]:
            x1 = line["Points"][0][0] # ???
            y1 = line["Points"][0][1] # ???
            x2 = line["Points"][1][0] # ???
            y2 = line["Points"][1][1] # ???
            speed = line["Speed"] # Miliseconds?

            distance = math.sqrt( ((x2-x1)**2) + ((y2-y1)**2) )
            line_time = distance * speed
            time += line_time
    return time

t1 = estimate("1_peca.gcode")
print(t1)

# Account for layer changes later

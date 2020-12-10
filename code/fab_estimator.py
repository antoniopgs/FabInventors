import datetime, math

def estimate(data):
    time = 0
    for layer in (x for x in data["layers"].values()):
        z2 = layer["z"]  # Milimeters
        for i, line in enumerate(layer["lines"]):
            if i != 0: # If not First Line of Layer.
                z1 = z2
            else: # If First Line of Layer.
                try:
                    z1 = data["layers"][i-1]["z"]
                except KeyError: # If no previous layer (means start of file)
                    z1 = 0
            x1 = line["Points"][0][0] # Milimeters
            y1 = line["Points"][0][1] # Milimeters
            x2 = line["Points"][1][0] # Milimeters
            y2 = line["Points"][1][1] # Milimeters
            speed = line["Speed"] / 60 # Milimeters Per Second

            distance = math.sqrt( ((x2-x1)**2) + ((y2-y1)**2) + ((z2-z1)**2) ) # Milimeters
            time += distance / speed # Seconds
            
    return datetime.timedelta(seconds=time)

"""
LATER:
- Account for lines with same position as previous line.
"""

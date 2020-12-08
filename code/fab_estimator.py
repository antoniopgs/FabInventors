import datetime, json, math

def estimate(data):
    time = 0
    for layer in (x for x in json.loads(data).values()):
        for line in layer["lines"]:
            x1 = line["Points"][0][0] # Milimeters
            y1 = line["Points"][0][1] # Milimeters
            x2 = line["Points"][1][0] # Milimeters
            y2 = line["Points"][1][1] # Milimeters
            speed = line["Speed"] / 60 # Milimeters Per Second

            distance = math.sqrt( ((x2-x1)**2) + ((y2-y1)**2) ) # Milimeters
            time += distance / speed # Seconds
            
    return datetime.timedelta(seconds=time)

"""
LATER:
- Account for lines with same position as previous line.
- Account for layer changes.
"""

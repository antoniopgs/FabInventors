from fab_timer import timer
import datetime, math

@timer
def estimate(data):
    time = 0 # Seconds
    for line in data["lines"]:
        x1 = line["points"][0][0] # Milimeters
        y1 = line["points"][0][1] # Milimeters
        z1 = line["points"][0][2] # Milimeters
        
        x2 = line["points"][1][0] # Milimeters
        y2 = line["points"][1][1] # Milimeters
        z2 = line["points"][1][2] # Milimeters
        
        speed = line["speed"] / 60 # Milimeters per Second

        distance = math.sqrt( ((x2-x1)**2) + ((y2-y1)**2) + ((z2-z1)**2) ) # Milimeters
        
        if distance > 0:
            time += distance / speed
        elif distance == 0:
            time += line["extrusion"] / speed # Not sure this is right...
            
    return datetime.timedelta(seconds=time)


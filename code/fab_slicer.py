from shapely.geometry import LineString, MultiLineString
from shapely.ops import split

def slice_json(json, slices = 3):
    output = {}
    
    min_x = min(line["points"][1][0] for line in json["lines"])
    max_x = max(line["points"][1][0] for line in json["lines"])
    
    min_y = min(line["points"][1][1] for line in json["lines"])
    max_y = max(line["points"][1][1] for line in json["lines"])
    
    slice_width = (max_x - min_x) / slices
    boundaries = []

    for i in range(1, slices):
        boundary = LineString([(min_x + i*slice_width, min_y), (min_x + i*slice_width, max_y)])
        boundaries.append(boundary)

    boundaries = MultiLineString(boundaries)

    for line in json["lines"]:
        lx1, ly1 = line["points"][0][0], line["points"][0][1]
        lx2, ly2 = line["points"][1][0], line["points"][1][1]
            
        line_str = LineString([(lx1,ly1), (lx2,ly2)])
        sublines = split(line_str, boundaries)

        for subline in list(sublines.geoms):
            subline_coords = list(subline.coords)
                
            sx1 = subline_coords[0][0]
            sy1 = subline_coords[0][1]
                
            sx2 = subline_coords[1][0]
            sy2 = subline_coords[1][1]

            for n in range(0, slices):
                output.setdefault(f"slice-{n+1}", {"input": f"Slice {n+1} of {json['input']}", "lines": []})
                
                left_bound = min_x + n*slice_width
                right_bound = min_x + (n+1)*slice_width

                if left_bound <= sx1 <= right_bound and left_bound <= sx2 <= right_bound:
                    subline = {"points": [(sx1,sy1, line["points"][0][2]),
                                          (sx2,sy2, line["points"][1][2])],
                               "speed": line["speed"], # Not sure if this is correct
                               "extrusion": line["extrusion"], # Not sure if this is correct
                               "type": line["type"],
                               "mesh": line["mesh"]} # Not sure if this is correct
                    output[f"slice-{n+1}"]["lines"].append(subline)

    return output

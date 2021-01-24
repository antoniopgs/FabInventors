from shapely.geometry import LineString, Polygon, MultiPolygon

def set_boundaries(json_data, rows, columns):
    min_x = min(line["points"][1][0] for line in json_data["lines"])
    max_x = max(line["points"][1][0] for line in json_data["lines"])
        
    min_y = min(line["points"][1][1] for line in json_data["lines"])
    max_y = max(line["points"][1][1] for line in json_data["lines"])

    slice_width = (max_x - min_x) / columns
    slice_depth = (max_y - min_y) / rows
    
    polygons = []

    for r in range(0, rows):
        for c in range(0, columns):
            bottom_left = (min_x + c*slice_width, min_y + r*slice_depth)
            bottom_right = (min_x + (c+1)*slice_width, min_y + r*slice_depth)
            top_right = (min_x + (c+1)*slice_width, min_y + (r+1)*slice_depth)
            top_left = (min_x + c*slice_width, min_y + (r+1)*slice_depth)
            
            polygon = Polygon([bottom_left, bottom_right, top_right, top_left])
            polygons.append(polygon)

    return MultiPolygon(polygons)

def slice_json(json_data, rows = 2, columns = 3):
    output = {}
    previous_travel = False
    for line in json_data["lines"]:

        lx1, ly1 = line["points"][0][0], line["points"][0][1]
        lx2, ly2 = line["points"][1][0], line["points"][1][1]
            
        line_str = LineString([(lx1,ly1), (lx2,ly2)])

        boundaries = set_boundaries(json_data, rows, columns)

        for i, boundary in enumerate(boundaries):
            output.setdefault(f"slice-{i+1}", {"input": f"Slice {i+1} of {json_data['input']}", "lines": []})
            sub_line_str = line_str.intersection(boundary)
            
            if not sub_line_str.is_empty:
                sub_line_str_coords = list(sub_line_str.coords)

                sx1 = sub_line_str_coords[0][0]
                sy1 = sub_line_str_coords[0][1]
                    
                sx2 = sub_line_str_coords[1][0]
                sy2 = sub_line_str_coords[1][1]

                # TRAVEL LINE STITCHER
                travel = True if line["type"] == "TRAVEL" else False
                if not previous_travel and travel: # If beginning to travel.
                    travel_sx1 = sx1 # current sub-line x1
                    travel_sy1 = sy1 # current sub-line y1
                    previous_travel = travel # Save Previous Travel value.
                    continue
                elif previous_travel and travel: # If still traveling.
                    continue
                elif previous_travel and not travel: # If just ended traveling.
                    travel_sx2 = sx1 # current sub-line x1
                    travel_sy2 = sy1 # current sub-line y1
                    travel_line = {"points": [(travel_sx1,travel_sy1, line["points"][0][2]),
                                              (travel_sx2,travel_sy2, line["points"][1][2])],
                                   "speed": line["speed"], # Not sure about speed here.
                                   "extrusion": float(0),
                                   "type": line["type"],
                                   "mesh": line["mesh"]}
                    output[f"slice-{i+1}"]["lines"].append(travel_line)
                    previous_travel = travel # Save Previous Travel value.

                # DIVIDE TOTAL LINE EXTRUSION PER SUB-LINES IF NEEDED:
                if line_str.length == 0:
                    sub_line_str_extrusion = line["extrusion"]
                else:
                    sub_line_str_extrusion = line["extrusion"] / (line_str.length / sub_line_str.length)

                output_line = {"points": [(sx1,sy1, line["points"][0][2]),
                                        (sx2,sy2, line["points"][1][2])],
                             "speed": line["speed"],
                             "extrusion": sub_line_str_extrusion,
                             "type": line["type"],
                             "mesh": line["mesh"]}

                output[f"slice-{i+1}"]["lines"].append(output_line)

    return output

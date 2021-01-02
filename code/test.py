from fab_visualizer import visualize
from fab_estimator import estimate
from fab_parser import parse

samples_folder = "./../gcode_samples/"
g_code = samples_folder + "1_peca.gcode"

json = parse(g_code)
plt = visualize(json)
estimation = estimate(json)

plt.show()
print(f"- Estimated Print Time: {estimation}")

'''
parsing_runtime = parse(g_code, True)
visualization_runtime = visualize(json, True)
estimation_runtime = estimate(json, True)

print(f"""- Parsing Runtime: {parsing_runtime}s
- Estimation Runtime: {estimation_runtime}s
- Visualization Runtime: {visualization_runtime}s""")
'''

import json
import pandas as pd

india_states = json.load(open(r"../../resource/states_india.geojson",'r'))
print(india_states['features'][1])

data = pd.read_csv("")
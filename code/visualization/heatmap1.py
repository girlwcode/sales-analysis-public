import json
import pandas as pd

india_states = json.load(open(r"../../resource/states_india.geojson",'r'))
print(india_states['features'][1])

data = pd.read_csv(r"../../resource/GeocodingData/Hospital/hospital in Assam, India_cleansed.csv_final.csv")
print(data.values)   #geocoding csv 하나 가져옴 (테스트용..)


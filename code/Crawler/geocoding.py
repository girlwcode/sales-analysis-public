import os
import pandas as pd

def find_latitude_longtitude(url):
    latitude_start_index = str(url).find('!3d')
    latitude_end_index = str(url).find('!4d')
    longtitude_start_index = str(url).find('!4d')
    longtitude_end_index = str(url).find('?')

    latitude = str(url)[latitude_start_index + 3: latitude_end_index]
    longtitude = str(url)[longtitude_start_index + 3: longtitude_end_index]

    return latitude, longtitude
    # return float(latitude), float(longtitude)

# Main
origin_dir = '../../resource/CleansedData/GoogleMap/'
for detail in os.listdir(origin_dir):
    # detail = ['Clinic','Fitness','Hospital']
    for csv_data in os.listdir(origin_dir + detail):
        file_name = os.path.basename(csv_data) + '_final.csv'
        data = pd.read_csv(origin_dir + detail + '/' + csv_data)
        # print(data.shape)
        # data.head()

        data['latitude'], data['longtitude'] = zip(*data['Url'].apply(find_latitude_longtitude))
        # data.head()

        save_dir = '../../resource/GeocodingData/' + detail + '/' + file_name
        data.to_csv(save_dir, index=False)

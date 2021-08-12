import os
import pandas as pd

def find_latitude_longitude(url):
    latitude_start_index = str(url).find('!3d')
    latitude_end_index = str(url).find('!4d')
    longitude_start_index = str(url).find('!4d')
    longitude_end_index = str(url).find('?')

    latitude = str(url)[latitude_start_index + 3: latitude_end_index]
    longitude = str(url)[longitude_start_index + 3: longitude_end_index]

    return latitude, longitude
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

        data['latitude'], data['longitude'] = zip(*data['Url'].apply(find_latitude_longitude))
        # data.head()

        save_dir = '../../resource/GeocodingData/' + detail + '/' + file_name
        data.to_csv(save_dir, index=False)

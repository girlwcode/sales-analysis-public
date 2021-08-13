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
    # return float(latitude), float(longitude)

def add_territory(file_name):
    if 'clinic' in file_name:
        file_name = file_name.replace('clinic in ', '')
        territory = file_name.replace(', India_cleansed', '')
    elif 'fitness' in file_name:
        file_name = file_name.replace('fitness in ', '')
        territory = file_name.replace(', India_cleansed', '')
    else:
        file_name = file_name.replace('hospital in ', '')
        territory = file_name.replace(', India_cleansed', '')

    return territory


# Main
origin_dir = '../../resource/CleansedData/GoogleMap/'
for detail in os.listdir(origin_dir):
    # detail = ['Clinic','Fitness','Hospital']
    for csv_data in os.listdir(origin_dir + detail):
        file_name = os.path.splitext(csv_data)[0]
        data = pd.read_csv(origin_dir + detail + '/' + csv_data)
        # print(data.shape)
        # data.head()

        data['Latitude'], data['Longitude'] = zip(*data['Url'].apply(find_latitude_longitude))
        # data.head()
        # territory 추가
        data['Territory'] = add_territory(file_name)

        save_dir = '../../resource/GeocodingData/'+detail+'/'+file_name+'_final.csv'
        data.to_csv(save_dir, index=False)

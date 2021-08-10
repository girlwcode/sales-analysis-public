import pandas as pd

keyw = 'clinic'
state = 'Assam'
keyw = pd.read_csv(r'C:\Users\Lenovo\PycharmProjects\new_cleansing\resource\CrawlingData\hospital in Uttarakhand, India.csv')

print(keyw.shape)
keyw.head()


def find_latitude_longtitude(url):
    latitude_start_index = url.find('!3d')
    latitude_end_index = url.find('!4d')
    longtitude_start_index = url.find('!4d')
    longtitude_end_index = url.find('?')

    latitude = url[latitude_start_index + 3: latitude_end_index]
    longtitude = url[longtitude_start_index + 3: longtitude_end_index]

    return float(latitude), float(longtitude)

keyw['latitude'], keyw['longtitude'] = zip(*keyw['Url'].apply(find_latitude_longtitude))
keyw.head()

save_dir = r'C:/Users/Lenovo/PycharmProjects/new_cleansing/resource/GeocodingData/hospital in Uttarakhand'+'.csv'
keyw.to_csv(save_dir, index=False)
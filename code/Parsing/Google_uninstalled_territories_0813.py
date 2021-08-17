import pandas  as pd


clinic = pd.read_csv('../../resource/GeocodingData/merge/Clinic_final.csv')
hospital = pd.read_csv('../../resource/GeocodingData/merge/Hospital_final.csv')
fitness = pd.read_csv('../../resource/GeocodingData/merge/Fitness_final.csv')

# Territory List
east = ['West Bengal','Assam','Tripura','Sikkim','Manipur','Nagaland','Arunachal Pradesh','Mizoram']
west1 = ['Maharashtra','Goa']
west2 = ['Gujarat','Rajasthan','Madhya Pradesh']
north = ['Uttar Pradesh','Delhi','Haryana','Punjab','Uttarakhand','Himachal Pradesh','Jammu and Kashmir','Chandigarh','Meghalaya' ]
south = ['Tamil Nadu','Karnataka','Andhra Pradesh','Telangana','Kerala','Puducherry' ]

east_df = pd.DataFrame(columns=['Company_Name','Category','Address','Url','Latitude','Longitude','State'])
west1_df = pd.DataFrame(columns=['Company_Name','Category','Address','Url','Latitude','Longitude','State'])
west2_df = pd.DataFrame(columns=['Company_Name','Category','Address','Url','Latitude','Longitude','State'])
north_df = pd.DataFrame(columns=['Company_Name','Category','Address','Url','Latitude','Longitude','State'])
south_df = pd.DataFrame(columns=['Company_Name','Category','Address','Url','Latitude','Longitude','State'])

for row in clinic.index:
    if clinic['State'][row] in east :
        east_df = east_df.append(clinic.iloc[row])
    elif clinic['State'][row] in west1 :
        west1_df = west1_df.append(clinic.iloc[row])
    elif clinic['State'][row] in west2 :
        west2_df = west2_df.append(clinic.iloc[row])
    elif clinic['State'][row] in north :
        north_df = north_df.append(clinic.iloc[row])
    else:
        south_df = south_df.append(clinic.iloc[row])

east_df.to_csv('../../resource/GeocodingData/Territory_category(uninstalled)/east_clinic_uninstalled.csv', index=False)
west1_df.to_csv('../../resource/GeocodingData/Territory_category(uninstalled)/west1_clinic_uninstalled.csv', index=False)
west2_df.to_csv('../../resource/GeocodingData/Territory_category(uninstalled)/west2_clinic_uninstalled.csv', index=False)
north_df.to_csv('../../resource/GeocodingData/Territory_category(uninstalled)/north_clinic_uninstalled.csv', index=False)
south_df.to_csv('../../resource/GeocodingData/Territory_category(uninstalled)/south_clinic_uninstalled.csv', index=False)

east_df = pd.DataFrame(columns=['Company_Name','Category','Address','Url','Latitude','Longitude','State'])
west1_df = pd.DataFrame(columns=['Company_Name','Category','Address','Url','Latitude','Longitude','State'])
west2_df = pd.DataFrame(columns=['Company_Name','Category','Address','Url','Latitude','Longitude','State'])
north_df = pd.DataFrame(columns=['Company_Name','Category','Address','Url','Latitude','Longitude','State'])
south_df = pd.DataFrame(columns=['Company_Name','Category','Address','Url','Latitude','Longitude','State'])


for row in hospital.index:
    if hospital['State'][row] in east :
        east_df = east_df.append(hospital.iloc[row])
    elif hospital['State'][row] in west1 :
        west1_df = west1_df.append(hospital.iloc[row])
    elif hospital['State'][row] in west2 :
        west2_df = west2_df.append(hospital.iloc[row])
    elif hospital['State'][row] in north :
        north_df = north_df.append(hospital.iloc[row])
    else:
        south_df = south_df.append(hospital.iloc[row])

east_df.to_csv('../../resource/GeocodingData/Territory_category(uninstalled)/east_hospital_uninstalled.csv', index=False)
west1_df.to_csv('../../resource/GeocodingData/Territory_category(uninstalled)/west1_hospital_uninstalled.csv', index=False)
west2_df.to_csv('../../resource/GeocodingData/Territory_category(uninstalled)/west2_hospital_uninstalled.csv', index=False)
north_df.to_csv('../../resource/GeocodingData/Territory_category(uninstalled)/north_hospital_uninstalled.csv', index=False)
south_df.to_csv('../../resource/GeocodingData/Territory_category(uninstalled)/south_hospital_uninstalled.csv', index=False)

east_df = pd.DataFrame(columns=['Company_Name','Category','Address','Url','Latitude','Longitude','State'])
west1_df = pd.DataFrame(columns=['Company_Name','Category','Address','Url','Latitude','Longitude','State'])
west2_df = pd.DataFrame(columns=['Company_Name','Category','Address','Url','Latitude','Longitude','State'])
north_df = pd.DataFrame(columns=['Company_Name','Category','Address','Url','Latitude','Longitude','State'])
south_df = pd.DataFrame(columns=['Company_Name','Category','Address','Url','Latitude','Longitude','State'])

for row in fitness.index:
    if fitness['State'][row] in east :
        east_df = east_df.append(fitness.iloc[row])
    elif fitness['State'][row] in west1 :
        west1_df = west1_df.append(fitness.iloc[row])
    elif fitness['State'][row] in west2 :
        west2_df = west2_df.append(fitness.iloc[row])
    elif fitness['State'][row] in north :
        north_df = north_df.append(fitness.iloc[row])
    else:
        south_df = south_df.append(fitness.iloc[row])

east_df.to_csv('../../resource/GeocodingData/Territory_category(uninstalled)/east_fitness_uninstalled.csv', index=False)
west1_df.to_csv('../../resource/GeocodingData/Territory_category(uninstalled)/west1_fitness_uninstalled.csv', index=False)
west2_df.to_csv('../../resource/GeocodingData/Territory_category(uninstalled)/west2_fitness_uninstalled.csv', index=False)
north_df.to_csv('../../resource/GeocodingData/Territory_category(uninstalled)/north_fitness_uninstalled.csv', index=False)
south_df.to_csv('../../resource/GeocodingData/Territory_category(uninstalled)/south_fitness_uninstalled.csv', index=False)

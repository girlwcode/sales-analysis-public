import pandas as pd

gdp = pd.read_csv('../../resource/External_Feature/GDP_final.csv')
hdi = pd.read_csv('../../resource/External_Feature/HDI_final.csv')

# gdp, hdi territory별로 평균내기
date_list = ['2017','2018','2019','2020','2021']

    # 'east': ['West Bengal', 'Assam', 'Tripura', 'Sikkim', 'Manipur', 'Nagaland', 'Arunachal Pradesh', 'Mizoram'],
    # 'west1': ['Maharashtra', 'Goa'],
    # 'west2': ['Gujarat', 'Rajasthan', 'Madhya Pradesh'],
    # 'north': ['Uttar Pradesh', 'Delhi', 'Haryana', 'Punjab', 'Uttarakhand', 'Himachal Pradesh', 'Jammu and Kashmir',
    #           'Chandigarh', 'Meghalaya'],
    # 'south': ['Tamil Nadu', 'Karnataka', 'Andhra Pradesh', 'Telangana', 'Kerala', 'Puducherry']

gdp_result = pd.DataFrame()
gdp_result['Date'] = date_list
hdi_result = pd.DataFrame()
hdi_result['Date'] = date_list

# gdp
gdp = gdp.iloc[16:21]
hdi = hdi.iloc[27:32]

east = gdp[['West Bengal', 'Assam', 'Tripura', 'Sikkim', 'Manipur', 'Nagaland', 'Arunachal Pradesh', 'Mizoram']]
gdp_result['East'] = list(east.mean(axis=1))
west1 = gdp[['Maharashtra', 'Goa']]
gdp_result['West 1'] = list(west1.mean(axis=1))
west2 = gdp[['Gujarat', 'Rajasthan', 'Madhya Pradesh']]
gdp_result['West 2'] = list(west2.mean(axis=1))
south = gdp[['Uttar Pradesh', 'Delhi', 'Haryana', 'Punjab', 'Uttarakhand', 'Himachal Pradesh', 'Jammu and Kashmir',
              'Chandigarh', 'Meghalaya']]
gdp_result['South'] = list(south.mean(axis=1))
north = gdp[['Tamil Nadu', 'Karnataka', 'Andhra Pradesh', 'Telangana', 'Kerala', 'Puducherry']]
gdp_result['North'] = list(north.mean(axis=1))

# print(gdp_result)
gdp_result.to_csv('../../resource/Score/Score_gdp.csv', index=False)

east = hdi[['West Bengal', 'Assam', 'Tripura', 'Sikkim', 'Manipur', 'Nagaland', 'Arunachal Pradesh', 'Mizoram']]
hdi_result['East'] = list(east.mean(axis=1))
west1 = hdi[['Maharashtra', 'Goa']]
hdi_result['West 1'] = list(west1.mean(axis=1))
west2 = hdi[['Gujarat', 'Rajasthan', 'Madhya Pradesh']]
hdi_result['West 2'] = list(west2.mean(axis=1))
south = hdi[['Uttar Pradesh', 'Delhi', 'Haryana', 'Punjab', 'Uttarakhand', 'Himachal Pradesh', 'Jammu and Kashmir',
              'Chandigarh', 'Meghalaya']]
hdi_result['South'] = list(south.mean(axis=1))
north = hdi[['Tamil Nadu', 'Karnataka', 'Andhra Pradesh', 'Telangana', 'Kerala', 'Puducherry']]
hdi_result['North'] = list(north.mean(axis=1))

# print(hdi_result)
hdi_result.to_csv('../../resource/Score/Score_hdi.csv', index=False)
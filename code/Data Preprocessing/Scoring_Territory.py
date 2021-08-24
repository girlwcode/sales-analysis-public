import pandas as pd

# Deal Success Rate
ds1 = pd.read_csv('../../resource/PlotCSV/Monthly Deal Success Rate By Territories East (2017-2021).csv')
ds2 = pd.read_csv('../../resource/PlotCSV/Monthly Deal Success Rate By Territories West1 (2017-2021).csv')
ds3 = pd.read_csv('../../resource/PlotCSV/Monthly Deal Success Rate By Territories West 2 (2017-2021).csv')
ds4 = pd.read_csv('../../resource/PlotCSV/Monthly Deal Success Rate By Territories South (2017-2021).csv')
ds5 = pd.read_csv('../../resource/PlotCSV/Monthly Deal Success Rate By Territories North (2017-2021).csv')
ds6 = pd.read_csv('../../resource/PlotCSV/Monthly Deal Success Rate By Territories Overseas (2017-2021).csv')
ds7 = pd.read_csv('../../resource/PlotCSV/Monthly Deal Success Rate By Territories Amazon (2017-2021).csv')
ds_list = [ds1, ds2, ds3, ds4, ds5, ds6, ds7]
terri_name_list = ['East', 'West 1', 'West 2', 'South', 'North', 'Overseas', 'Amazon']

date_list = list(ds1['x'])

for i, df in enumerate(ds_list):
    del df['x']
    df.rename(columns={'y': terri_name_list[i]}, inplace=True)
ds_full = pd.concat(ds_list, axis=1)
ds_full = ds_full * 100
ds_full = ds_full.replace(0, 1)
# print(ds_full)

# Average Sales per Deal
asd1 = pd.read_csv('../../resource/PlotCSV/Monthly Average Sales By Territories East (2017-2021).csv')
asd2 = pd.read_csv('../../resource/PlotCSV/Monthly Average Sales By Territories West 1 (2017-2021).csv')
asd3 = pd.read_csv('../../resource/PlotCSV/Monthly Average Sales By Territories West 2 (2017-2021).csv')
asd4 = pd.read_csv('../../resource/PlotCSV/Monthly Average Sales By Territories South (2017-2021).csv')
asd5 = pd.read_csv('../../resource/PlotCSV/Monthly Average Sales By Territories North (2017-2021).csv')
asd6 = pd.read_csv('../../resource/PlotCSV/Monthly Average Sales By Territories Overseas (2017-2021).csv')
asd7 = pd.read_csv('../../resource/PlotCSV/Monthly Average Sales By Territories Amazon (2017-2021).csv')

asd_list = [asd1, asd2, asd3, asd4, asd5, asd6, asd7]
for i, df in enumerate(asd_list):
    del df['x']
    df.rename(columns={'y': terri_name_list[i]}, inplace=True)
asd_full = pd.concat(asd_list, axis=1)

# Average Sales per Deal 퍼센트로 변환
asd_full['Sum'] = asd_full.sum(axis=1)

for col in asd_full.columns:
    asd_full[col] = asd_full[col].div(asd_full['Sum'])
del asd_full['Sum']
asd_full = asd_full.fillna(0)
asd_full = asd_full * 100
asd_full = asd_full.replace(0,1)
# print(asd_full)

terri_score = ds_full * asd_full
terri_score.insert(0, 'Date', date_list)
terri_score.to_csv('../../resource/Score/Score_Territory.csv', index=False)
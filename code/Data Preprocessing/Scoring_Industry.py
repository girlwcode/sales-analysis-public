import pandas as pd

# Sales Success Rate
ss1 = pd.read_csv('../../resource/PlotCSV/Monthly Sales Success Rate By Industry Academic, Private Enterprise, Hotel (2017-2021).csv')
ss2 = pd.read_csv('../../resource/PlotCSV/Monthly Sales Success Rate By Industry Hospital, Clinic, Fitness (2017-2021).csv')
ss3 = pd.read_csv('../../resource/PlotCSV/Monthly Sales Success Rate By Industry Military, Others_Individual, Others_etc (2017-2021).csv')
ss4 = pd.read_csv('../../resource/PlotCSV/Monthly Sales Success Rate By Industry Others_Others Corporate, Public Association, Others_Aesthetic (2017-2021).csv')

date_list = list(ss1['x'])
del ss1['x']
del ss2['x']
del ss3['x']
del ss4['x']
ss_full = pd.concat([ss1,ss2,ss3,ss4], axis=1)
ss_full = ss_full.replace(0,1)
# print(ss_full)


# Deal Success Rate
ds1 =  pd.read_csv('../../resource/PlotCSV/Monthly Deal Success Rate By Industry Academic, Private Enterprise, Hotel (2017-2021).csv')
ds2 =  pd.read_csv('../../resource/PlotCSV/Monthly Deal Success Rate By Industry Hospital, Clinic, Fitness (2017-2021).csv')
ds3 =  pd.read_csv('../../resource/PlotCSV/Monthly Deal Success Rate By Industry Military, Others_Individual, Others_etc (2017-2021).csv')
ds4 =  pd.read_csv('../../resource/PlotCSV/Monthly Deal Success Rate By Industry Others_Others Corporate, Public Association, Others_Aesthetic (2017-2021).csv')

del ds1['x']
del ds2['x']
del ds3['x']
del ds4['x']
ds_full = pd.concat([ds1, ds2, ds3, ds4], axis=1)
ds_full = ds_full * 100
ds_full = ds_full.replace(0,1)
# print(ds_full)


# Average Sales per Deal
asd1 = pd.read_csv('../../resource/PlotCSV/Monthly Average Sales By Industry Academic, Private Enterprise, Hotel (2017-2021).csv')
asd2 = pd.read_csv('../../resource/PlotCSV/Monthly Average Sales By Industry Hospital, Clinic, Fitness (2017-2021).csv')
asd3 = pd.read_csv('../../resource/PlotCSV/Monthly Average Sales By Industry Military, Others_Individual, Others_etc (2017-2021).csv')
asd4 = pd.read_csv('../../resource/PlotCSV/Monthly Average Sales By Industry Others_Others Corporate, Public Association, Others_Aesthetic (2017-2021).csv')

del asd1['x']
del asd2['x']
del asd3['x']
del asd4['x']
asd_full = pd.concat([asd1, asd2, asd3, asd4], axis=1)

# Average Sales per Deal 퍼센트로 변환
asd_full['Sum'] = asd_full.sum(axis=1)
# print(asd_full)

for col in asd_full.columns:
    asd_full[col] = asd_full[col].div(asd_full['Sum'])
del asd_full['Sum']
asd_full = asd_full.fillna(0)
asd_full = asd_full * 100
asd_full = asd_full.replace(0,1)
# print(asd_full)

industry_score = ss_full * ds_full * asd_full
industry_score.insert(0, 'Date', date_list)


industry_score.to_csv('../../resource/Score/Score_Industry.csv', index=False)

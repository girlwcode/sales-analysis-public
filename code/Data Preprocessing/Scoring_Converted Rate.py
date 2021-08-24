import pandas as pd

# Converted Rate By Industry concat
cr1 = pd.read_csv('../../resource/PlotCSV/Monthly Converted Rate By Industry Academic, Private Enterprise, Hotel (2017-2021).csv')
cr2 = pd.read_csv('../../resource/PlotCSV/Monthly Converted Rate By Industry Hospital, Clinic, Fitness (2017-2021).csv')
cr3 = pd.read_csv('../../resource/PlotCSV/Monthly Converted Rate By Industry Military, Others_Individual, Others_etc (2017-2021).csv')
cr4 = pd.read_csv('../../resource/PlotCSV/Monthly Converted Rate By Industry Others_Others Corporate, Public Association, Others_Aesthetic (2017-2021).csv')
date_list = list(cr1['x'])
del cr1['x']
del cr2['x']
del cr3['x']
del cr4['x']

convert_score = pd.concat([cr1,cr2,cr3,cr4], axis=1)
convert_score = convert_score * 100
convert_score = convert_score.replace(0,1)
convert_score.insert(0, 'Date', date_list)

convert_score.to_csv('../../resource/Score/Score_ConvertedRate.csv', index=False)
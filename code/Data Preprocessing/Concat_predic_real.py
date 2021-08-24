import pandas as pd

gdp_real = pd.read_csv('../../resource/External_Feature/GDP_transpose.csv')
gdp_predic = pd.read_csv('../../resource/External_Feature/GDP_prediction.csv')

hdi_real = pd.read_csv('../../resource/External_Feature/HDI_transpose.csv')
hdi_predic = pd.read_csv('../../resource/External_Feature/HDI_prediction.csv')

gdp = gdp_predic.iloc[1:]
gdp.rename(columns={'Unnamed: 0':'Date'}, inplace=True)
# print(gdp.columns)
gdp_full = pd.concat([gdp_real,gdp], ignore_index=True)

hdi = hdi_predic.iloc[1:]
hdi.rename(columns={'Unnamed: 0':'Date'}, inplace=True)
# print(gdp.columns)
hdi_full = pd.concat([hdi_real, hdi], ignore_index=True)

gdp_full.to_csv('../../resource/External_Feature/GDP_final.csv', index=False)
hdi_full.to_csv('../../resource/External_Feature/HDI_final.csv', index=False)
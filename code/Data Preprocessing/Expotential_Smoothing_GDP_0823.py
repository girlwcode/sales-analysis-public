import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt


gdp = pd.read_csv('../../resource/External_Feature/GDP_India_modified.csv')
# hdi = pd.read_csv('../../resource/External_Feature/HDI_India.csv')

'''
# GDP Plot 한번 찍어봄
x = range(2001, 2021)
count = 0
for i in gdp.index:
    if count == 4:
        break
    y = gdp.iloc[i,:].tolist()
    state = y.pop(0)
    if y[18] == None:
        y[18] = 0
    if y[19] == None:
        y[19] = 0
    plt.plot(x, y)
    plt.title(state+'_GDP')
    # plt.show()
    plt.savefig('../../resource/Plot_External/'+state+'_gdp.png')
    plt.cla()
    count+=1
'''

x = range(2001, 2021)
state_list = []
gdp_list = []
for i in gdp.index:
    y = gdp.iloc[i,:].tolist()
    state = y.pop(0)
    state_list.append(state)
    gdp_list.append(y)

gdp_new = pd.DataFrame()
gdp_new['Date'] = x

for i, state in enumerate(state_list):
    gdp_new[state] = gdp_list[i]

gdp_new.to_csv('../../resource/External_Feature/GDP_transpose.csv', index=False)


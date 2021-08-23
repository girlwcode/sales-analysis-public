import pandas as pd
import matplotlib.pyplot as plt


gdp = pd.read_csv('../../resource/External_Feature/GDP_India_modified.csv')
hdi = pd.read_csv('../../resource/External_Feature/HDI_India.csv')


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


# GDP row-column transpose
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


# HDI row-column transpose
x = range(1990, 2020)
state_list = []
hdi_list = []
for i in hdi.index:
    y = hdi.iloc[i,:].tolist()
    state = y.pop(0)
    state_list.append(state)
    hdi_list.append(y)

hdi_new = pd.DataFrame()
hdi_new['Date'] = x

for i, state in enumerate(state_list):
    hdi_new[state] = hdi_list[i]

hdi_new.to_csv('../../resource/External_Feature/HDI_transpose.csv', index=False)


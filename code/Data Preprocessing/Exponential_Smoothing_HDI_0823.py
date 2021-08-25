import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt

hdi = pd.read_csv('../../resource/External_Feature/HDI_India.csv')
gdp = pd.read_csv('../../resource/External_Feature/GDP_transpose.csv')
# ['Total', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Chandigarth', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh',
#  'Jammu and Kashmir', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland',
#  'New Delhi', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana',
#  'Tripura', 'Uttar Pradesh', 'Uttaranchal', 'West Bengal']
# print(hdi['State'].tolist())

"""
Plot HDI
x = range(1990, 2020)
y = []
count = 0
for i in hdi.index:
    if count == 4:
        break
    y = hdi.iloc[i,:].tolist()
    state = y.pop(0)
    plt.plot(x, y)
    plt.title(state+'_HDI')
    # plt.show()
    plt.savefig('../../resource/Plot_External/'+state+'_hdi.png')
    plt.cla()
    count+=1
"""
# Index(['Date', 'India', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Goa',
#        'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir',
#        'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
#        'Meghalaya', 'Mizoram', 'Nagaland', 'Punjab', 'Rajasthan', 'Sikkim',
#        'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand',
#        'West Bengal', 'Chandigarh', 'Delhi', 'Puducherry'],
#       dtype='object')
# print(gdp.columns.tolist())

# Simple Expotential Smoothing
# , initialization_method="heuristic"
# initialization_method="estimated"
def SimpleEx(data) :
    # fit1 = SimpleExpSmoothing(data, "heuristic").fit(smoothing_level=0.2,optimized=False)
    fit1 = SimpleExpSmoothing(data, initialization_method="heuristic").fit(smoothing_level=0.2,optimized=False)
    fcast1 = fit1.forecast(3).rename(r'$\alpha=0.2$')
    fit2 = SimpleExpSmoothing(data, initialization_method="heuristic").fit(smoothing_level=0.6,optimized=False)
    fcast2 = fit2.forecast(3).rename(r'$\alpha=0.6$')
    fit3 = SimpleExpSmoothing(data, initialization_method="estimated").fit()
    fcast3 = fit3.forecast(3).rename(r'$\alpha=%s$'%fit3.model.params['smoothing_level'])

    plt.figure(figsize=(12, 8))
    plt.plot(data, marker='o', color='black')
    plt.plot(fit1.fittedvalues, marker='o', color='blue')
    line1, = plt.plot(fcast1, marker='o', color='blue')
    plt.plot(fit2.fittedvalues, marker='o', color='red')
    line2, = plt.plot(fcast2, marker='o', color='red')
    plt.plot(fit3.fittedvalues, marker='o', color='green')
    line3, = plt.plot(fcast3, marker='o', color='green')
    plt.legend([line1, line2, line3], [fcast1.name, fcast2.name, fcast3.name])

# Holt's Method
def HoltMethod(data) :
    fit1 = Holt(data, initialization_method="estimated").fit(smoothing_level=0.8, smoothing_trend=0.2, optimized=False)
    fcast1 = fit1.forecast(5).rename("Holt's linear trend")
    fit2 = Holt(data, exponential=True, initialization_method="estimated").fit(smoothing_level=0.8, smoothing_trend=0.2, optimized=False)
    fcast2 = fit2.forecast(5).rename("Exponential trend")
    fit3 = Holt(data, damped_trend=True, initialization_method="estimated").fit(smoothing_level=0.8, smoothing_trend=0.2)
    fcast3 = fit3.forecast(5).rename("Additive damped trend")

    plt.figure(figsize=(12, 8))
    plt.plot(data, marker='o', color='black')
    plt.plot(fit1.fittedvalues, color='blue')
    line1, = plt.plot(fcast1, marker='o', color='blue')
    plt.plot(fit2.fittedvalues, color='red')
    line2, = plt.plot(fcast2, marker='o', color='red')
    plt.plot(fit3.fittedvalues, color='green')
    line3, = plt.plot(fcast3, marker='o', color='green')
    plt.legend([line1, line2, line3], [fcast1.name, fcast2.name, fcast3.name])




states = ['India', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh',
         'Jammu and Kashmir', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram',
         'Nagaland', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana',
         'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Chandigarh', 'Delhi', 'Puducherry']

for state in states:
    index = pd.date_range(start='2001', end='2019', freq='A')
    gdpData = pd.Series(gdp[state],index)
    SimpleEx(gdpData)

def MSE(data, fit1, fit2, fit3):
    mse1 =  sum((data - fit1.fittedvalues) ** 2) * 1 / len(data)
    mse2 = sum((data - fit2.fittedvalues) ** 2) * 1 / len(data)
    mse3 = sum((data - fit3.fittedvalues) ** 2) * 1 / len(data)

    m = min(mse1, mse2, mse3)

    if (m == mse1) :
        return fit1.forecast(5)
    elif (m == mse2) :
        return fit2.forecast(5)
    elif (m == mse3) :
        return fit3.forecast(5)




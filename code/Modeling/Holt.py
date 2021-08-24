"""
Holt를 사용하여 코로나가 없었다면, 매출 예측
사용 데이터 : 2017.1 - 2020.2 (37개월)
예측 : 2020.3 - 2022.7 (28개월)
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt

revenue = pd.read_csv('../../resource/Model_Input/Monthly_net.csv')

# 시나리오1 : 코로나가 없었더라면 매출 예측, 코로나 전 데이터만 사용 (2017.1-2020.2)
revenue_beforeCovid = revenue[pd.DatetimeIndex(revenue['Date']).year != 2021]
revenue_beforeCovid = revenue_beforeCovid.drop(revenue_beforeCovid.index[-10:])
revenue_beforeCovid['Date'] = pd.to_datetime(revenue_beforeCovid['Date'])
print(revenue_beforeCovid)

def SimpleES(df):
    fit1 = SimpleExpSmoothing(df, initialization_method="heuristic").fit(smoothing_level=0.2,optimized=False)
    fcast1 = fit1.forecast(16).rename(r'$\alpha=0.2$')
    fit2 = SimpleExpSmoothing(df, initialization_method="heuristic").fit(smoothing_level=0.6,optimized=False)
    fcast2 = fit2.forecast(16).rename(r'$\alpha=0.6$')
    fit3 = SimpleExpSmoothing(df, initialization_method="estimated").fit()
    fcast3 = fit3.forecast(16).rename(r'$\alpha=%s$'%fit3.model.params['smoothing_level'])

    plt.figure(figsize=(12, 8))
    plt.plot(df, marker='o', color='black')
    plt.plot(fit1.fittedvalues, marker='o', color='blue')
    line1, = plt.plot(fcast1, marker='o', color='blue')
    plt.plot(fit2.fittedvalues, marker='o', color='red')
    line2, = plt.plot(fcast2, marker='o', color='red')
    plt.plot(fit3.fittedvalues, marker='o', color='green')
    line3, = plt.plot(fcast3, marker='o', color='green')
    plt.legend([line1, line2, line3], [fcast1.name, fcast2.name, fcast3.name])
    plt.show()

def HoltMethod(data) :
    fit1 = Holt(data, initialization_method="estimated").fit(smoothing_level=0.8, smoothing_trend=0.2, optimized=False)
    fcast1 = fit1.forecast(16).rename("Holt's linear trend")
    fit2 = Holt(data, exponential=True, initialization_method="estimated").fit(smoothing_level=0.8, smoothing_trend=0.2, optimized=False)
    fcast2 = fit2.forecast(16).rename("Exponential trend")
    fit3 = Holt(data, damped_trend=True, initialization_method="estimated").fit(smoothing_level=0.8, smoothing_trend=0.2)
    fcast3 = fit3.forecast(16).rename("Additive damped trend")

    plt.figure(figsize=(12, 8))
    plt.plot(data, marker='o', color='black')
    plt.plot(fit1.fittedvalues, color='blue')
    line1, = plt.plot(fcast1, marker='o', color='blue')
    plt.plot(fit2.fittedvalues, color='red')
    line2, = plt.plot(fcast2, marker='o', color='red')
    plt.plot(fit3.fittedvalues, color='green')
    line3, = plt.plot(fcast3, marker='o', color='green')
    plt.legend([line1, line2, line3], [fcast1.name, fcast2.name, fcast3.name])
    plt.show()

    # return fit1, fit2, fit3


revenue_beforeCovid['Date'] = revenue_beforeCovid['Date'].replace('-','.')
y = revenue_beforeCovid['Net'].tolist()
x = revenue_beforeCovid['Date'].tolist()
df_hdi = pd.Series(y, x)
HoltMethod(df_hdi)
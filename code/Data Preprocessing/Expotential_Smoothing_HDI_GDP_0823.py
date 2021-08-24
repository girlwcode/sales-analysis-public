import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt


gdp = pd.read_csv('../../resource/External_Feature/GDP_transpose.csv')
hdi = pd.read_csv('../../resource/External_Feature/HDI_transpose.csv')

# SimpleExpSmoothing
def SimpleES(df):
    fit1 = SimpleExpSmoothing(df, initialization_method="heuristic").fit(smoothing_level=0.2,optimized=False)
    fcast1 = fit1.forecast(3).rename(r'$\alpha=0.2$')
    fit2 = SimpleExpSmoothing(df, initialization_method="heuristic").fit(smoothing_level=0.6,optimized=False)
    fcast2 = fit2.forecast(3).rename(r'$\alpha=0.6$')
    fit3 = SimpleExpSmoothing(df, initialization_method="estimated").fit()
    fcast3 = fit3.forecast(3).rename(r'$\alpha=%s$'%fit3.model.params['smoothing_level'])

    plt.figure(figsize=(12, 8))
    plt.plot(df, marker='o', color='black')
    plt.plot(fit1.fittedvalues, marker='o', color='blue')
    line1, = plt.plot(fcast1, marker='o', color='blue')
    plt.plot(fit2.fittedvalues, marker='o', color='red')
    line2, = plt.plot(fcast2, marker='o', color='red')
    plt.plot(fit3.fittedvalues, marker='o', color='green')
    line3, = plt.plot(fcast3, marker='o', color='green')
    plt.legend([line1, line2, line3], [fcast1.name, fcast2.name, fcast3.name])
    # plt.show()


# Holt
def HoltMethod(data):
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
    # plt.show()

    return fit1, fit2, fit3


def MSE(data, fit1, fit2, fit3):
    mse1 = sum((data - fit1.fittedvalues) ** 2) * 1 / len(data)
    mse2 = sum((data - fit2.fittedvalues) ** 2) * 1 / len(data)
    mse3 = sum((data - fit3.fittedvalues) ** 2) * 1 / len(data)

    print('[MSE] fit 1 :', mse1, ', fit 2 :', mse2, ', fit 3 :', mse3)
    m = min(mse1, mse2, mse3)

    if m == mse1:
        return m, fit1.forecast(5)
    elif m == mse2:
        bestModel = 'fit2'
        return m, fit2.forecast(5)
    elif m == mse3:
        bestModel = 'fit3'
        return m, fit3.forecast(5)

def MAE(data, fit1, fit2, fit3):
    mae1 = sum(abs(data - fit1.fittedvalues)) * 1 / len(data)
    mae2 = sum(abs(data - fit2.fittedvalues)) * 1 / len(data)
    mae3 = sum(abs(data - fit3.fittedvalues)) * 1 / len(data)

    # sse1 = fit1.sse
    # sse2 = fit2.sse
    # sse3 = fit3.sse

    print('[MSE] fit 1 :', mae1, ', fit 2 :', mae2, ', fit 3 :', mae3)
    m = min(mae1, mae2, mae3)

    if m == mae1:
        return m, fit1.forecast(5)
    elif m == mae2:
        return m, fit2.forecast(5)
    elif m == mae3:
        return m, fit3.forecast(5)

# Main
hdi_dict = {}
index_hdi = pd.date_range(start='1990', end='2020', freq='A')
for state in hdi.columns:
    if state == 'Date':
        continue
    y_hdi = hdi[state].tolist()
    df_hdi = pd.Series(y_hdi, index_hdi)

    fit1_hdi, fit2_hdi, fit3_hdi = HoltMethod(df_hdi)

    mse_hdi, bestValue_hdi = MAE(y_hdi, fit1_hdi, fit2_hdi, fit3_hdi)

    # print(bestModel+'\n'+bestValue)
    bestValue_hdi = list(bestValue_hdi)
    data_list1 = [mse_hdi]
    data_list1.extend(bestValue_hdi)
    hdi_dict[state] = data_list1


gdp_dict = {}
index_gdp = pd.date_range(start='2001', end='2019', freq='A')
for state in gdp.columns:
    if state == 'Date':
        continue

    y_gdp = gdp[state].tolist()
    df_gdp = pd.Series(y_gdp, index_gdp)

    fit1_gdp, fit2_gdp, fit3_gdp = HoltMethod(df_gdp)

    mse_gdp, bestValue_gdp = MAE(y_gdp, fit1_gdp, fit2_gdp, fit3_gdp)

    bestValue_gdp = list(bestValue_gdp)
    data_list2 = [mse_gdp]
    data_list2.extend(bestValue_gdp)
    gdp_dict[state] = data_list2

hdi_df = pd.DataFrame(hdi_dict, index=['best MAE',2020,2021,2022,2023,2024])
gdp_df = pd.DataFrame(gdp_dict, index=['best MAE',2019,2020,2021,2022,2023])

print('HDI prediction MSE(MEAN) : ', hdi_df.iloc[0].mean())
print('GDP prediction MSE(MEAN) : ', gdp_df.iloc[0].mean())

hdi_df.to_csv('../../resource/External_Feature/HDI_prediction.csv')
gdp_df.to_csv('../../resource/External_Feature/GDP_prediction.csv')

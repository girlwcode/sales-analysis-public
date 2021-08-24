"""
Prophet
1. 코로나가 없었다면, 매출 예측
2. 현 상황 데이터로 1년 예측
"""

import pandas as pd
from fbprophet import Prophet
from sklearn.metrics import mean_absolute_error
from matplotlib import pyplot as plt

# 데이터 로드
revenue = pd.read_csv('../../resource/Model_Input/Monthly_net.csv')

# 컬럼명 변경
revenue.rename(columns = {'Date' : 'ds'}, inplace = True)
revenue.rename(columns = {'Net':'y'}, inplace = True)

# print(revenue)
# 데이터 타입 변경
revenue['ds'] = pd.to_datetime(revenue['ds'])

# 시나리오1 : 코로나가 없었더라면 매출 예측, 코로나 전 데이터만 사용 (2017.1-2020.2)
revenue_beforeCovid = revenue[pd.DatetimeIndex(revenue['ds']).year != 2021]
revenue_beforeCovid = revenue_beforeCovid.drop(revenue_beforeCovid.index[-10:])
print(revenue_beforeCovid)


# test_y = revenue_beforeCovid['y'][-12:].values
# test_x = revenue_beforeCovid['ds'][-12:].values
# test_x = pd.DataFrame(test_x, columns=['ds'])
# train = revenue_beforeCovid.drop(revenue_beforeCovid.index[-12:])


model = Prophet()
model.fit(revenue_beforeCovid)

future = model.make_future_dataframe(periods=24, freq='MS')
predict = model.predict(future)
plot = model.plot(predict)
plot

# pred = predict['yhat'].values
# mae = mean_absolute_error(test_y, pred)
# #MAE: 2540011.464
# print('MAE: %.3f' % mae)

#Plot the Results
# plt.plot(test_y, label='Actual')
# plt.plot(pred, label='Predicted')
# plt.legend()
# plt.show()

# # 모델 생성
# model = Prophet(yearly_seasonality=True)
#
# # 모델 학습
# model.fit(revenue)

#
#
# last_1year = ['2020.8','2020.9','2020.10','2020.11','2020.12','2021.1',
#               '2021.2','2021.3','2021.4','2021.5','2021.6','2021.7']
# last_1year = pd.DataFrame(last_1year, columns=['ds'])
#
# last_1year['ds'] = pd.to_datetime((last_1year['ds']))
#
# # predict = model.predict(last_1year)
# #
# # model.plot(predict)
# # plt.show()
#
# # 마지막 1년을 제외하고 학습 진행, test = 1년 (2020.8-2021.7)
# train = revenue.drop(revenue.index[-12:])
# y_true = revenue['y'][-12:].values
#
# # 모델 생성 후 학습
# model = Prophet()
# model.fit(train)
#
# predict = model.predict(last_1year)
# y_pred = predict['yhat'].values
#
#
#
# mae = mean_absolute_error(y_true, y_pred)
# print('MAE: %.3f' % mae)
# MAE: 2965447.370
# MAE: 2540011.464
# # Plot the Results
# plt.plot(y_true, label='Actual')
# plt.plot(y_pred, label='Predicted')
# plt.legend()
# plt.show()
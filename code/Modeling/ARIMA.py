"""
ARIMA를 사용하여 코로나가 없었다면, 매출 예측
사용 데이터 : 2017.1 - 2020.2 (37개월)
예측 : 2020.3 - 2022.7 (28개월)
"""
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

revenue = pd.read_csv('../../resource/Model_Input/Monthly_net.csv', header=0, index_col=0, squeeze=True)
revenue_beforeCovid = pd.read_csv('../../resource/Model_Input/Monthly_Net_BeforeCorona.csv', header=0, index_col=0, squeeze=True)
revenue_beforeCovid.plot()

# 시나리오1 : 코로나가 없었더라면 매출 예측, 코로나 전 데이터만 사용 (2017.1-2020.2)
# revenue_beforeCovid = revenue[pd.DatetimeIndex(revenue['Date']).year != 2021]
# revenue_beforeCovid = revenue_beforeCovid.drop(revenue_beforeCovid.index[-10:])
# revenue_beforeCovid['Date'] = pd.to_datetime(revenue_beforeCovid['Date'])
# print(revenue_beforeCovid)
# plt.plot(revenue_beforeCovid['Date'],revenue_beforeCovid['Net'])
# plt.show()
# plot_acf(revenue_beforeCovid)
# plot_pacf(revenue_beforeCovid)
# plt.show()

# diff_1=revenue_beforeCovid.diff(periods=1).iloc[1:]
# diff_1.plot()
# plot_acf(diff_1)
# plot_pacf(diff_1)
# plt.show()

from statsmodels.tsa.arima_model import ARIMA

model = ARIMA(revenue_beforeCovid, order=(0,1,1))
model_fit = model.fit(trend='c',full_output=True, disp=1)
print(model_fit.summary())

model_fit.plot_predict()
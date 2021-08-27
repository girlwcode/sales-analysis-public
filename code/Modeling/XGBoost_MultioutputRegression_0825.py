"""
시나리오 2 : Multi output Regression with XGBoost 활용하여 해당 달의 추후 12개월간의 매출 예측
"""
import pandas as pd
from sklearn import preprocessing
from sklearn.multioutput import MultiOutputRegressor
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import xgboost as xgb
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold
from xgboost import plot_importance, plot_tree
from xgboost import XGBRegressor

# Load the Dataset
test_num = 3
if test_num == 1:
    # Test1 - Extracted Feature
    revenue = pd.read_csv('../../resource/Model_Input/Monthly_zoho.csv')
    features_considered = ['DealScore', 'LeadScore', 'ConvertedRate', 'DealNum', 'LeadNum', 'Net']
    revenue = revenue[features_considered]
elif test_num == 2:
    # Test2 - Full set
    revenue = pd.read_csv('../../resource/Model_Input/Monthly_zoho_numeric.csv')
    features_considered = ['IndustryNumeric', 'TerritoryNumeric', 'ConvertedRate', 'DealNum', 'LeadNum', 'Net']
    revenue = revenue[features_considered]
elif test_num == 3:
    # Test3 - Extracted Feature + Extra Factor
    revenue = pd.read_csv('../../resource/Model_Input/Monthly_googleTrend.csv')
    features_considered = ['DealScore',	'LeadScore', 'ConvertedRate', 'DealNum', 'LeadNum', 'GoogleTrend', 'Net']
    revenue = revenue[features_considered]

# Min-Max Scaling
scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
scaler = scaler.fit(revenue) #값을 0~1로 떨어뜨린다
scaled = scaler.transform(revenue) #값을 0~1로 떨어뜨린다
scaled = pd.DataFrame(scaled,columns=features_considered)

# Data Split
x = []
y = []
for row in scaled.index :
    if (row+13 <= len(scaled)):
        x.append(scaled.iloc[row])
        y.append(list(revenue.iloc[row+1:row+13, -1]))
    else: break

x = pd.DataFrame(x)
y = pd.DataFrame(y)

## 학습과 테스트 데이터 분리
# 43개 - 34 (train), 9 (test)
train_X = x[:34]
train_y = y[:34]
test_X = x[34:]
test_y = y[34:]
# print(train_y)

## Modeling
model = MultiOutputRegressor(xgb.XGBRegressor(n_estimators=1000, learning_rate=0.05, gamma=0, subsample=0.75,
                           colsample_bytree=1, max_depth=7))

# define model evaluation method
# 5-fold
cv = RepeatedKFold(n_splits=5, n_repeats=10, random_state=1)
scores = cross_val_score(model, x, y, scoring='neg_mean_absolute_error', cv=cv, n_jobs=-1)
# force scores to be positive
scores = np.absolute(scores)
print('Mean MAE of Cross Validations : %.3f (%.3f)' % (scores.mean(), scores.std()) )
model.fit(train_X, train_y)


# evaluate model
y_pred = model.predict(test_X)
# # print(y_pred)
# # print(train_y.iloc[1])
plt.plot(range(1,13), test_y.iloc[3], label='real')
plt.plot(range(1,13), y_pred[3], label='predict')
plt.legend()
plt.show()

# XG_model_month = xgb.XGBRegressor(n_estimators=1000)
# XG_model_month.fit(df_train_x, df_train_y, eval_set=[(df_test_x, df_test_y)], early_stopping_rounds=50,verbose=False)

# # 주요하게 적용하는 변수를 판단
# plot_importance(XG_model_month, height=0.9)

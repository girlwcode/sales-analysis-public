"""
시나리오 3 : Multi output Regression with SVM 활용하여 해당 달의 추후 12개월간의 매출 예측
"""
# Import module
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.multioutput import MultiOutputRegressor
from sklearn.svm import SVR
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold
from sklearn.metrics  import mean_squared_error, r2_score, mean_absolute_error, mean_squared_log_error

# Load the Dataset
test_num = 1
if test_num == 1:
    # Test1 - Extracted Feature
    revenue = pd.read_csv('../../resource/Model_Input/Monthly_zoho.csv')
    features_considered = ['DealScore', 'LeadScore', 'ConvertedRate', 'DealNum', 'LeadNum', 'Net']
    revenue = revenue[features_considered]
    C = 500
    gamma = 'auto'
elif test_num == 2:
    # Test2 - Full set
    revenue = pd.read_csv('../../resource/Model_Input/Monthly_zoho_numeric.csv')
    features_considered = ['IndustryNumeric', 'TerritoryNumeric', 'ConvertedRate', 'DealNum', 'LeadNum', 'Net']
    revenue = revenue[features_considered]
    C = 600
    gamma = 1
elif test_num == 3:
    # Test3 - Extracted Feature + Extra Factor
    revenue = pd.read_csv('../../resource/Model_Input/Monthly_googleTrend.csv')
    features_considered = ['DealScore',	'LeadScore', 'ConvertedRate', 'DealNum', 'LeadNum', 'GoogleTrend', 'Net']
    revenue = revenue[features_considered]
    C = 600
    gamma = 1

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

# Split the Dataset
# 43개 - 34 (train), 9 (test)
train_X = x[:34]
train_y = y[:34]
test_X = x[34:]
test_y = y[34:]
# print(train_y.shape)

# Modeling
model = MultiOutputRegressor(SVR(C=500, gamma=300))
model.fit(train_X, train_y)
r_sq = model.score(train_X, train_y)
print(r_sq)

# define model evaluation method
# evaluate model
model = MultiOutputRegressor(SVR(C=500, gamma=300))
cv = RepeatedKFold(n_splits=5, n_repeats=10, random_state=1)
scores = cross_val_score(model, x, y, scoring='neg_mean_absolute_error', cv=cv, n_jobs=-1)
# force scores to be positive
scores = np.absolute(scores)
print('Mean MAE of Cross Validations : %.3f (%.3f)' % (scores.mean(), scores.std()) )
model.fit(train_X, train_y)

y_pred = model.predict(test_X)
score = model.score(test_X, test_y)
print('R square value of prediction : ',score)
# # print(y_pred)
# # print(train_y.iloc[1])
for i in range (0,9) :
  plt.plot(range(1,13), test_y.iloc[0], label='real')
  plt.plot(range(1,13), y_pred[3], label='predict')
  plt.legend()
  plt.show()


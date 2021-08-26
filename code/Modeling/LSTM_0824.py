"""
시나리오 1 : LSTM을 활용하여 앞으로 12개월간의 매출 예측
"""

# Import module
import numpy as np
import pandas as pd
from sklearn import preprocessing

# Load the Dataset
revenue = pd.read_csv('../../resource/Model_Input/Monthly_net.csv')
revenue['Date'] = pd.to_datetime(revenue['Date'])

revenue['year'] = pd.DatetimeIndex(revenue['Date']).year
revenue['month'] = pd.DatetimeIndex(revenue['Date']).month

features_considered = ['year','month','Net']
print(len(revenue))
revenue = revenue[features_considered]
revenue.to_csv('../../resource/Model_Input/Input.csv',index=False)
# print(revenue)


# Min-Max Scaling
scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
scaled = scaler.fit_transform(revenue) #값을 0~1로 떨어뜨린다
# print(scaled)


## Set window size (input, output)
# reshape input to be 3D [samples, timesteps, features]
reframed_X =[]
reframed_Y = []
n_future = 12
n_past = 12
print(scaled[:,2])

for i in range(n_past, len(scaled)-n_future+1):
    reframed_X.append(scaled[i-n_past:i, 0:scaled.shape[1]])
    reframed_Y.append(scaled[i:i+n_future, 2])

reframed_X, reframed_Y = np.array(reframed_X), np.array(reframed_Y)
print(reframed_X.shape)
print(reframed_Y.shape)
print(reframed_Y)


# # Split the Data
# n_train_len = round(len(reframed_X) * 0.8,0) -> 26
train_X = reframed_X[:26, :]
train_y = reframed_Y[:26, :]
test_X = reframed_X[26:, :]
test_y = reframed_Y[26:, :]

print(train_X.shape)
print(train_y.shape)


# Modeling
import keras
from keras.layers import LSTM
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from tensorflow.keras.optimizers import Adam # - Works
from keras.layers import RepeatVector
from keras.layers import TimeDistributed

# Many to Many
# train the model
def build_model(train_x, train_y):
	n_timesteps, n_features, n_outputs = train_x.shape[1], train_x.shape[2], train_y.shape[1]
	# reshape output into [samples, timesteps, features]
	train_y = train_y.reshape((train_y.shape[0], train_y.shape[1], 1))
	# define model
	model = Sequential()
	model.add(LSTM(100, activation='relu', input_shape=(n_timesteps, n_features)))
	model.add(RepeatVector(n_outputs))
	model.add(LSTM(120, activation='relu', return_sequences=True))
	model.add(TimeDistributed(Dense(12, activation='relu')))
	model.add(TimeDistributed(Dense(1)))
	model.compile(loss='mse', optimizer='adam')
	# fit network
	return model

print(train_y.shape)
# define parameters
verbose, epochs, batch_size = 1, 100, 3

model = build_model(train_X,train_y)
model.fit(train_X, train_y, epochs=epochs, batch_size=batch_size, verbose=2)

import matplotlib.pyplot as plt
pred_y = model.predict(test_X,verbose=1)
score = model.evaluate(test_X, test_y,verbose=1)
print(score)
# loss: 0.0602 -> month,year 로 했을 때
# loss: 0.0817 -> 우리 feature
#loss: 0.0766
# loss: 0.0566
# loss: 0.0573
for i in range(0,6):
  pred1 = np.array(pred_y[i]).flatten()
  plt.plot(range(1,13),test_y[i],label='real')
  plt.plot(range(1,13),pred1,label='predict')
  plt.legend()
  plt.show()
# score = model.evaluate(test_X, test_y, batch_size=128)

## 시나리오 2 : Multioutput Regression with SVM 활용하여 해당 달의 추후 12개월간의 매출 예측
# Import module
import numpy as np
import pandas as pd
from sklearn import preprocessing

revenue = pd.read_csv('../../resource/Model_Input/Monthly_net.csv')
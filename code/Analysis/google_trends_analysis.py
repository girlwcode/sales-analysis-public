import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../../resource/GoogleTrends/google_trends_monthly_mean.csv')

plt.plot(data['Date'],data['Interest Level'])
plt.show()
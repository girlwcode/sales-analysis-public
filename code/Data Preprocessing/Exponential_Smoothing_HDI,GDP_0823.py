import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

hdi = pd.read_csv('../../resource/External_Feature/HDI_India.csv')

# ['Total', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Chandigarth', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh',
#  'Jammu and Kashmir', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland',
#  'New Delhi', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana',
#  'Tripura', 'Uttar Pradesh', 'Uttaranchal', 'West Bengal']

print(hdi['State'].tolist())

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
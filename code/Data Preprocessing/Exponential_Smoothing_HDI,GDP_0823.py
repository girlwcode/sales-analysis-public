import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

hdi = pd.read_csv('../../resource/External_Feature/HDI_India.csv')

# ['Total', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Chandigarth', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh',
#  'Jammu and Kashmir', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland',
#  'New Delhi', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana',
#  'Tripura', 'Uttar Pradesh', 'Uttaranchal', 'West Bengal']
print(hdi['State'].tolist())
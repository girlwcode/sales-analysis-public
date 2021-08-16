import pandas as pd
import matplotlib.pyplot as plt
import collections

clinic = pd.read_csv('../../resource/GeocodingData/merge/Clinic_final2.csv')
hospital = pd.read_csv('../../resource/GeocodingData/merge/Hospital_final2.csv')
fitness = pd.read_csv('../../resource/GeocodingData/merge/Fitness_final2.csv')

clinic = clinic.dropna(axis=0)

clinic_counter = collections.Counter(clinic['Territory'])
fitness_counter = collections.Counter(fitness['Territory'])
hospital_counter = collections.Counter(hospital['Territory'])

plt.figure(figsize=(12,6))
plt.subplot(131)
plt.title('Clinic', fontsize=13)
x = clinic_counter.keys()
y = list(clinic_counter.values())
plt.bar(x, y)
for i, x_ in enumerate(x):
    plt.text(x_, y[i], y[i],
             fontsize=9,
             color='black',
             horizontalalignment='center',
             verticalalignment='bottom')

plt.subplot(132)
plt.title('Hospital', fontsize=13)
x = hospital_counter.keys()
y = list(hospital_counter.values())
plt.bar(x, y)
for i, x_ in enumerate(x):
    plt.text(x_, y[i], y[i],
             fontsize=9,
             color='black',
             horizontalalignment='center',
             verticalalignment='bottom')

plt.subplot(133)
plt.title("Fitness", fontsize=13)
x = fitness_counter.keys()
y = list(fitness_counter.values())
plt.bar(x, y)
for i, x_ in enumerate(x):
    plt.text(x_, y[i], y[i],
             fontsize=9,
             color='black',
             horizontalalignment='center',
             verticalalignment='bottom')

plt.savefig('../../resource/Plot/Google by category.png')
plt.show()

print(clinic['State'].unique())

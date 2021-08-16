import pandas as pd
import collections
import matplotlib.pyplot as plt
import numpy as np

deals = pd.read_csv('../../resource/CleansedData/Zoho CRM/Potentials_001_fillTerritories_final.csv')
deals_before = pd.read_csv('../../resource/CRM_OriginalData/Potentials_001.csv')

leads = pd.read_csv('../../resource/CleansedData/Zoho CRM/Leads_001_IndustryCleansed.csv')
leads_before = pd.read_csv('../../resource/CRM_OriginalData/Leads_001.csv')

contacts = pd.read_csv('../../resource/CleansedData/Zoho CRM/Contacts_001_fillTerritories_final.csv')
contacts_fin = collections.Counter(contacts['Territories'])
print(contacts_fin)

deals_before = deals_before.replace(np.nan, 'nan', regex=True)
deals_terri_before = collections.Counter(deals_before['Territory'])
print(deals_terri_before)

deals_territories = collections.Counter(deals['Territory_fin'])
print(deals_territories)

leads_before = leads_before.replace(np.nan, 'nan', regex=True)
leads_ids_before = collections.Counter(leads_before['Industry'])
print(leads_ids_before)

leads_territories = collections.Counter(leads['Industry Fin'])
print(leads_territories)

plt.figure(1,figsize=(5,5))
plt.title('Contacts After Cleansing (Territory)',fontsize=15)
l = contacts_fin.items()
l = sorted(l)
x,y = zip(*l)
plt.bar(x,y)
for i, x_ in enumerate(x):
    plt.text(x_, y[i], y[i],
             fontsize=9,
             color='black',
             horizontalalignment='center',
             verticalalignment='bottom')
plt.savefig('../../resource/Plot/Contacts After Cleansing (Territory).png')

plt.figure(2, figsize=(13,5))
plt.subplot(121)
plt.title('Deals Before Cleansing (Territory)',fontsize=15)
l = deals_terri_before.items()
l = sorted(l)
x,y = zip(*l)
plt.bar(x,y)
for i, x_ in enumerate(x):
    plt.text(x_, y[i], y[i],
             fontsize=9,
             color='black',
             horizontalalignment='center',
             verticalalignment='bottom')


plt.subplot(122)
plt.title('Deals After Cleansing (Territory)',fontsize=15)
l = deals_territories.items()
l = sorted(l)
x,y = zip(*l)
plt.bar(x,y)
for i, x_ in enumerate(x):
    plt.text(x_, y[i], y[i],
             fontsize=9,
             color='black',
             horizontalalignment='center',
             verticalalignment='bottom')

plt.savefig('../../resource/Plot/Deals After Cleansing (Territory).png')
plt.show()

plt.figure(3, figsize=(5,10))
plt.title('Leads After Cleansing (Industry)',fontsize=15)
l = leads_territories.items()
l = sorted(l)
x,y = zip(*l)
plt.bar(x,y)
plt.xticks(rotation=90, ha= 'center')
for i, x_ in enumerate(x):
    plt.text(x_, y[i], y[i],
             fontsize=9,
             color='black',
             horizontalalignment='center',
             verticalalignment='bottom')

# plt.savefig('../../resource/Plot/Leads After Cleansing (Industry).png')
plt.show()
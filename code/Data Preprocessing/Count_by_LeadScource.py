import pandas as pd
import matplotlib.pyplot as plt

leads = pd.read_csv('../../resource/CleansedData/ZohoCRM/Leads_001_IndustryCleansed.csv')
deals = pd.read_csv('../../resource/CleansedData/ZohoCRM/Potentials_001_fillIndustry.csv')


# print('Deal에서 총 source 개수', len(deals['Lead Source'].unique()))
# print('Lead에서 총 source 개수', len(leads['Lead Source'].unique()))
# print('')

def count_source(df, month_dict, contains_str):
    df_new = df[df['Stage'].str.contains(contains_str)]
    for source in df_new['Lead Source'].unique():
        if str(source) == 'nan':
            month_dict[str(source)] = df_new['Lead Source'].isna().sum()
        else:
            month_dict[str(source)] = len(df_new[df_new['Lead Source']==source])


# Potentials By Monthly
deals['Created Time'] = pd.to_datetime(deals['Created Time'])
dict_keys = list(deals['Lead Source'].unique())
dict_keys.insert(0, 'Date')

plus_df = pd.DataFrame(columns=dict_keys)
minus_df = pd.DataFrame(columns=dict_keys)

years = range(2017, 2022)
months = range(1, 13)
for year in years:
    if year == 2021:
        months = range(1, 8)
    for month in months:
        plus_dict = dict.fromkeys(dict_keys)
        minus_dict = dict.fromkeys(dict_keys)
        plus_dict['Date'] = str(year)+'-'+str(month)
        minus_dict['Date'] = str(year) + '-' + str(month)
        df = deals[(deals['Created Time'].dt.year == year) & (deals['Created Time'].dt.month == month)]
        if not df.empty:
            count_source(df, plus_dict, '5|6|7|Deposit')
            count_source(df, minus_dict, '8|10|Rejected')

        plus_df = plus_df.append(plus_dict, ignore_index=True)
        minus_df = minus_df.append(minus_dict, ignore_index=True)

plus_df.to_csv('../../resource/Score/Deal_leadSource_Plus_Count.csv', index=False)
minus_df.to_csv('../../resource/Score/Deal_leadSource_Minus_Count.csv', index=False)

# Leads By Monthly
leads['Created Time'] = pd.to_datetime(leads['Created Time'])
leads.rename(columns={'Lead Status':'Stage'}, inplace=True)
dict_keys = list(leads['Lead Source'].unique())
dict_keys.insert(0, 'Date')

plus_df = pd.DataFrame(columns=dict_keys)
minus_df = pd.DataFrame(columns=dict_keys)

years = range(2017, 2022)
months = range(1, 13)
for year in years:
    if year == 2021:
        months = range(1, 8)
    for month in months:
        plus_dict = dict.fromkeys(dict_keys)
        minus_dict = dict.fromkeys(dict_keys)
        plus_dict['Date'] = str(year)+'-'+str(month)
        minus_dict['Date'] = str(year) + '-' + str(month)
        df = leads[(leads['Created Time'].dt.year == year) & (leads['Created Time'].dt.month == month)]
        if not df.empty:
            count_source(df, plus_dict, '2|9|10')
            count_source(df, minus_dict, '1|6|7')

        plus_df = plus_df.append(plus_dict, ignore_index=True)
        minus_df = minus_df.append(minus_dict, ignore_index=True)

plus_df.to_csv('../../resource/Score/Lead_leadSource_Plus_Count.csv', index=False)
minus_df.to_csv('../../resource/Score/Lead_leadSource_Minus_Count.csv', index=False)

'''
# Potential Stage(5,6,7,Deposit) Lead Source 분포 -> 가중치+
deals_plus = deals[deals['Stage'].str.contains('5|6|7|Deposit')]

plus_dict = {}
for source in deals_plus['Lead Source'].unique():
    if str(source) == 'nan':
        plus_dict[str(source)] = deals_plus['Lead Source'].isna().sum()
    else:
        plus_dict[str(source)] = len(deals_plus[deals_plus['Lead Source']==source])
title = 'Closed Deal'
print(title,'\nsource 개수:', len(plus_dict))

fig,ax = plt.subplots()
plt.title(title)
x = plus_dict.keys()
y = list(plus_dict.values())
plt.bar(x,y)
for i, x_ in enumerate(x):
    plt.text(x_, y[i], y[i],
             fontsize=9,
             color='black',
             horizontalalignment='center',
             verticalalignment='bottom')
ax.set_xticklabels(x)
fig.autofmt_xdate(rotation=45)
plt.savefig('../../resource/Plot_Scoring/'+title+'.png')
# plt.show()


# Potential Stage(8,10,Rejected) Lead Source 분포 -> 가중치-
deals_minus = deals[deals['Stage'].str.contains('8|10|Rejected')]

minus_dict = {}
for source in deals_minus['Lead Source'].unique():
    if str(source) == 'nan':
        minus_dict[str(source)] = deals_minus['Lead Source'].isna().sum()
    else:
        minus_dict[str(source)] = len(deals_minus[deals_minus['Lead Source']==source])
title = 'Loss Deal'
print(title,'\nsource 개수:', len(minus_dict))

fig,ax = plt.subplots()
plt.title(title)
x = minus_dict.keys()
y = list(minus_dict.values())
plt.bar(x,y)
for i, x_ in enumerate(x):
    plt.text(x_, y[i], y[i],
             fontsize=9,
             color='black',
             horizontalalignment='center',
             verticalalignment='bottom')
ax.set_xticklabels(x)
fig.autofmt_xdate(rotation=45)
plt.savefig('../../resource/Plot_Scoring/'+title+'.png')
# plt.show()


# Leads Lead Status(2,9,19) Lead Source 분포 -> 가중치+
leads_plus = leads[leads['Lead Status'].str.contains('2|9|10')]

plus_dict = {}
for source in leads_plus['Lead Source'].unique():
    if str(source) == 'nan':
        plus_dict[str(source)] = leads_plus['Lead Source'].isna().sum()
    else:
        plus_dict[str(source)] = len(leads_plus[leads_plus['Lead Source']==source])
title = 'Good Lead'
print(title,'\nsource 개수:', len(plus_dict))

fig,ax = plt.subplots()
plt.title(title)
x = plus_dict.keys()
y = list(plus_dict.values())
plt.bar(x,y)
for i, x_ in enumerate(x):
    plt.text(x_, y[i], y[i],
             fontsize=9,
             color='black',
             horizontalalignment='center',
             verticalalignment='bottom')
ax.set_xticklabels(x)
fig.autofmt_xdate(rotation=45)
plt.savefig('../../resource/Plot_Scoring/'+title+'.png')
# plt.show()


# Leads Lead Status(1,6,7) Lead Source 분포 -> 가중치-
leads_minus = leads[leads['Lead Status'].str.contains('1|6|7')]

minus_dict = {}
for source in leads_minus['Lead Source'].unique():
    if str(source) == 'nan':
        minus_dict[str(source)] = leads_minus['Lead Source'].isna().sum()
    else:
        minus_dict[str(source)] = len(leads_minus[leads_minus['Lead Source']==source])
title = 'Bad Lead'
print(title,'\nsource 개수:', len(minus_dict))

fig,ax = plt.subplots()
plt.title(title)
x = minus_dict.keys()
y = list(minus_dict.values())
plt.bar(x,y)
for i, x_ in enumerate(x):
    plt.text(x_, y[i], y[i],
             fontsize=9,
             color='black',
             horizontalalignment='center',
             verticalalignment='bottom')
ax.set_xticklabels(x)
fig.autofmt_xdate(rotation=45)
plt.savefig('../../resource/Plot_Scoring/'+title+'.png')
# plt.show()
'''
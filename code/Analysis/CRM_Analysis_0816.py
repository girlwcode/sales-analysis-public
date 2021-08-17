import pandas as pd
import matplotlib.pyplot as plt
import dataframe as df

sales_17 = pd.read_csv('../../resource/SalesData/Installation_2017.csv')
sales_18 = pd.read_csv('../../resource/SalesData/Installation_2018.csv')
sales_19 = pd.read_csv('../../resource/SalesData/Installation_2019.csv')
sales_20 = pd.read_csv('../../resource/SalesData/Installation_2020.csv')
sales_21 = pd.read_csv('../../resource/SalesData/Installation_2021.csv')

leads = pd.read_csv('../../resource/CleansedData/Zoho CRM/Leads_001_IndustryCleansed.csv')
deals = pd.read_csv('../../resource/CleansedData/Zoho CRM/Potentials_001_fillTerritories_final.csv')

print(sales_17.columns)

# 순 이익 : 17,18 - Actual Value, 19,20,21 - Net
revenue_17 = sales_17.loc[:,['Month','Region','Category','Actual Value']]
revenue_18 = sales_18.loc[:,['Month','Region','Category','Actual Value']]
revenue_19 = sales_19.loc[:,['Month','Region','Category','Net']]
revenue_20 = sales_20.loc[:,['Month','Region','Category','Net']]
revenue_21 = sales_21.loc[:,['Month','Region','Category','Net']]

# Lead, Deal 월별로 구분
lead = leads.loc[:,['Lead Source','Lead Status','Created Time','Industry Fin']]
deal = deals.loc[:,['Amount','Stage','Lead Source','Created Time','Territory_fin']]

# 날짜 DateTime으로 변경
lead['Created Time'] = pd.to_datetime(lead['Created Time'])
deal['Created Time'] = pd.to_datetime(deal['Created Time'])

# year, month 열 추가
lead['year'] = pd.DatetimeIndex(lead['Created Time']).year
lead['month'] = pd.DatetimeIndex(lead['Created Time']).month

deal['year'] = pd.DatetimeIndex(deal['Created Time']).year
deal['month'] = pd.DatetimeIndex(deal['Created Time']).month

print(lead)
print(deal)

# 컬럼명 변경
revenue_17.rename(columns = {'Actual Value' : 'Net'}, inplace = True)
revenue_18.rename(columns = {'Actual Value' : 'Net'}, inplace = True)


# Nan 값 0으로
revenue_17['Net'] = revenue_17['Net'].fillna(0)
revenue_18['Net'] = revenue_18['Net'].fillna(0)
revenue_19['Net'] = revenue_19['Net'].fillna(0)
revenue_20['Net'] = revenue_20['Net'].fillna(0)
revenue_21['Net'] = revenue_21['Net'].fillna(0)

# print(revenue_17['Region'].unique())

years = [revenue_17, revenue_18, revenue_19, revenue_20, revenue_21]
months = ['January','February','March','April','May','June','July','August','September','October','November','December']
regions = ['West 1','South','North','East','West 2']
rev_year = {}

# revenue_monthly
year = 2017
cnt = 1
for y in years :
    plt.cla()
    # print(year)
    revenue = {}
    mt = 1
    if (cnt == 5):
        months =  ['January','February','March','April','May','June','July']
    for m in months :
        r = sum(y[y['Month'] == m]['Net'])
        revenue[m] = r
        key = str(year) + '.' + str(mt)
        rev_year[key] = r
        mt += 1
    # print(revenue)
    # title = 'Revenue of '+str(year)
    # plt.figure(figsize=(12, 7))
    # plt.title(title, fontsize=15)
    # plt.plot(list(revenue.keys()), list(revenue.values()))
    # plt.savefig('../../resource/Plot/'+title+'(monthly).png')
    year += 1
    cnt += 1



# revenue_territory
year = 2017
for y in years :
    plt.cla()
    year += 1
    # print(revenue)
    # print(year)
    revenue = {}
    for re in regions :
        r = sum(y[y['Region'] == re]['Net'])
        revenue[re] = r
    title = 'Revenue of '+str(year)
    # plt.figure(figsize=(10, 7))
    # plt.title(title, fontsize=15)
    # plt.plot(list(revenue.keys()), list(revenue.values()))
    # plt.savefig('../../resource/Plot/'+title+'(territory).png')


# lead 갯수
l = {}
year = [2017,2018,2019,2020,2021]
month = [1,2,3,4,5,6,7,8,9,10,11,12]
for y in year:
    if (y == 2021):
        month = [1, 2, 3, 4, 5, 6, 7]
    for m in month:
        cnt = 0
        for row in lead.index :
            if (lead['year'][row] == y and lead['month'][row] == m) :
                cnt +=1
            key = str(y) +'.'+str(m)
            l[key] = cnt

# deal 갯수
d = {}
year = [2017,2018,2019,2020,2021]
month = [1,2,3,4,5,6,7,8,9,10,11,12]
for y in year:
    if (y == 2021):
        month = [1, 2, 3, 4, 5, 6, 7]
    for m in month:
        cnt = 0
        for row in deal.index :
            if (deal['year'][row] == y and deal['month'][row] == m) :
                cnt +=1
            key = str(y) +'.'+str(m)
            d[key] = cnt

plt.plot(list(d.keys()), list(d.values()))
plt.title('Whole Deals per months of Inbody, India', fontsize=18)
plt.xticks(rotation=90)
plt.show()

# Whole revenue
x = list(rev_year.keys())
y1 = list(rev_year.values())
y2 = list(l.values())

fig, ax1 = plt.subplots()
ax1.plot(x, y1, color='deeppink', label='Revenue')
fig.autofmt_xdate(rotation=90)
ax1.legend(loc='upper right')

ax2 = ax1.twinx()
ax2.plot(x, y2, color='green', label='Leads')
ax1.legend(loc='lower right')

plt.title('Whole Revenue and leads of Inbody, India', fontsize=18)
plt.legend()
plt.show()

# Leads and Deals
x = list(d.keys())
y1 = list(d.values())
y2 = list(l.values())

fig, ax1 = plt.subplots()
ax1.plot(x, y1, color='deeppink', label='Deals')
fig.autofmt_xdate(rotation=90)
ax1.legend(loc='upper right')

ax2 = ax1.twinx()
ax2.plot(x, y2, color='green', label='Leads')
ax1.legend(loc='lower right')

plt.title('Whole Deals and leads of Inbody, India', fontsize=18)
plt.legend()
plt.show()


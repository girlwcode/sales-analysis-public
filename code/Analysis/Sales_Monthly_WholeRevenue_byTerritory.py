import pandas as pd
import matplotlib.pyplot as plt
#원본 csv
wholeRevenue = pd.read_csv(r"C:\Users\Lenovo\PycharmProjects\new_cleansing\resource\SalesData\Whole Revenue.csv")
wholeRevenue = pd.DataFrame(wholeRevenue)
wholeRevenue

months = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,
          'October':10,'November':11,'December':12}

for row in wholeRevenue.index :
    for month in months.keys():
        if (wholeRevenue['Month'][row] == month):
            wholeRevenue['Month'][row] = months[month]

#south
regionList =['West 1' ,'South', 'North', 'East', 'West 2', 'Overseas', 'Amazon', 'West 1 ']
onlysouth =wholeRevenue[wholeRevenue['Region'] == 'South']


# onlysouth['sum_net'] = onlysouth['net'].sum()
onlysouth.head()

#north
onlynorth =wholeRevenue[wholeRevenue['Region'] == 'North']
onlynorth.head()

#west1
onlywest1 =wholeRevenue[wholeRevenue['Region'] == 'West 1']
onlywest1.head()

#west2
onlywest2 =wholeRevenue[wholeRevenue['Region'] == 'West 2']
onlywest2.tail()

#east
onlyeast =wholeRevenue[wholeRevenue['Region'] == 'East']
onlyeast.head()

#overseas
onlyoverseas =wholeRevenue[wholeRevenue['Region'] == 'Overseas']
onlyoverseas.head()

#amazon
onlyamazon =wholeRevenue[wholeRevenue['Region'] == 'Amazon']
onlyamazon.head()

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
years = [2017,2018,2019,2020,2021]
regions = [onlywest1,onlywest2, onlysouth, onlynorth, onlyeast, onlyoverseas, onlyamazon]
titles = ['West1','West2','South','North','East','Overseas','Amazon']

cnt = 0
for region in regions:
    revenue = {}
    for y in years:
        for m in months:
            condition1 = region['Year'] == y
            condition2 = region['Month'] == m
            r = sum(region[condition1 & condition2]['Net'])
            key = str(y) + '-' + str(m)
            revenue[key] = r
    plt.figure(figsize=(15, 8))
    plt.title('Monthly Whole Revenue By Territories:'+titles[cnt]+' (2017-2021)', fontsize=20)
    plt.plot(list(revenue.keys()), list(revenue.values()))
    plt.xticks(rotation=90)
    plt.ylabel('Rs', fontsize=12)
    title = 'Monthly Whole Revenue By Territories '+str(titles[cnt])+' (2017-2021)'
    save_dir = '../../resource/Plot/' + title
    plt.savefig(save_dir + '.png')
    save_dir = '../../resource/PlotCSV/' + title
    rev = pd.DataFrame(list(revenue.items()),
                   columns=['x', 'y'])
    rev.to_csv(save_dir+'.csv',index=False)
    cnt += 1
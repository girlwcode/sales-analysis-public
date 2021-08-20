import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import collections

# territory 결측치 Handling
revenue_origin = pd.read_csv('../../resource/SalesData/Whole Revenue_fillIndustry.csv')

# 6건
# print(revenue['Region'].isnull().sum())

# 직원 선물 5건 삭제 - Net:0
revenue_origin = revenue_origin.drop(revenue_origin[revenue_origin['Category']=='Employee Gift'].index, axis=0)

# Inbody 본사 이벤트 - 본사(West 1)
idx = revenue_origin[revenue_origin['Client'] == 'InBody Challenge'].index
revenue_origin.at[idx,'Region']= 'West 1'
revenue_origin.to_csv('../../resource/SalesData/Whole Revenue_fillTerritory.csv')


# Whole Sales 분석
revenue = pd.read_csv('../../resource/SalesData/Whole Revenue_fillTerritory.csv')

## 1. Territory 별 총 Sales
months = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,
          'October':10,'November':11,'December':12}

for row in revenue.index :
    for month in months.keys():
        if (revenue['Month'][row] == month):
            revenue['Month'][row] = months[month]


months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
territories = ['West 1','West 2','South','North','East','Overseas','Amazon']
years = [2017,2018,2019,2020,2021]
cnt = 0

for territory in territories :
    rev_terri = revenue[revenue['Region']==territory]
    rev = {}
    for y in years:
        if (y == 2021):
            months= [1, 2, 3, 4, 5, 6, 7]
        for m in months:
            condition1 = rev_terri['Year'] == y
            condition2 = rev_terri['Month'] == m
            r = sum(rev_terri[condition1 & condition2]['Net'])
            key = str(y) + '-' + str(m)
            rev[key] = r
    plt.figure(figsize=(15, 8))
    plt.title('Monthly Whole Revenue By Territories:' + territory + ' (2017-2021)', fontsize=20)
    plt.plot(list(rev.keys()), list(rev.values()))
    plt.xticks(rotation=90)
    plt.ylabel('Rs', fontsize=12)
    title = 'Monthly Whole Revenue By Territories ' + str(territory) + ' (2017-2021)'
    save_dir = '../../resource/Plot/' + title
    plt.savefig(save_dir + '.png')
    save_dir = '../../resource/PlotCSV/' + title
    rev = pd.DataFrame(list(rev.items()),
                       columns=['x', 'y'])
    rev.to_csv(save_dir + '.csv', index=False)


# Industry 별 총 Sales
# [figure1] hopital, clinic, fitness
# [figure2] acdemic, private enterprise, hotel
# [figure3] others-others coporate, public association, others-aesthetic
# [figure4] millitary, others-individual, others-etc

# ['Clinic' 'Fitness' 'Hospital' 'Others_Aesthetic' 'Private Enterprise'
#  'Others_Others Corporate' 'Hotel' 'Others_etc' 'Others_Individual'
#  'Academic' 'Public Association' 'Military']
# print(revenue['Industry Fin'].unique())

print(collections.Counter(revenue['Industry Fin']))
industries = [['Hospital','Clinic','Fitness'],['Academic','Private Enterprise','Hotel'],
              ['Others_Others Corporate','Public Association','Public Association'],
              ['Military','Others_Individual','Others_etc']]

for industry in industries:
    rev_ids1 = revenue[revenue['Industry Fin'] == industry[0]]
    rev_ids2 = revenue[revenue['Industry Fin'] == industry[1]]
    rev_ids3 = revenue[revenue['Industry Fin'] == industry[2]]
    rev1 = {}
    rev2 = {}
    rev3 = {}
    for y in years:
        if (y == 2021):
            months= [1, 2, 3, 4, 5, 6, 7]
        for m in months:
            key = str(y) + '-' + str(m)
            condition1 = rev_ids1['Year'] == y
            condition2 = rev_ids1['Month'] == m
            r = sum(rev_ids1[condition1 & condition2]['Net'])
            rev1[key] = r

            condition1 = rev_ids2['Year'] == y
            condition2 = rev_ids2['Month'] == m
            r = sum(rev_ids2[condition1 & condition2]['Net'])
            rev2[key] = r

            condition1 = rev_ids3['Year'] == y
            condition2 = rev_ids3['Month'] == m
            r = sum(rev_ids3[condition1 & condition2]['Net'])
            rev3[key] = r

    plt.figure(figsize=(15, 8))
    plt.bar(list(rev1.keys()), list(rev1.values()), color='green', label = industry[0])
    plt.bar(list(rev1.keys()), list(rev2.values()), color='blue',bottom=np.array(list(rev1.values())), label = industry[1])
    plt.bar(list(rev1.keys()), list(rev3.values()), color='red', bottom=np.array(list(rev1.values()))+np.array(list(rev2.values())), label = industry[2])
    plt.legend()
    name = industry[0] +', ' +industry[1] + ', ' +industry[2]
    plt.title('Monthly Whole Revenue By Industry:' + name + ' (2017-2021)', fontsize=20)
    plt.xticks(rotation=90)
    plt.ylabel('Rs', fontsize=12)
    title = 'Monthly Whole Revenue By Industry ' + str(name) + ' (2017-2021)'
    save_dir = '../../resource/Plot/' + title
    plt.savefig(save_dir + '.png')
    save_dir = '../../resource/PlotCSV/' + title
    data = {
        'x':list(rev1.keys()),
        industry[0]:list(rev1.values()),
        industry[1]: list(rev2.values()),
        industry[2]: list(rev3.values())
    }
    rev = pd.DataFrame(data)
    rev.to_csv(save_dir + '.csv', index=False)





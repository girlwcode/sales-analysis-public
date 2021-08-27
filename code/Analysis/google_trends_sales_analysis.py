import pandas as pd
import matplotlib.pyplot as plt

trends = pd.read_csv('../../resource/GoogleTrends/Google_trends_monthly_avg.csv')
sales = pd.read_csv('../../resource/SalesData/Whole Revenue_fillTerritory.csv')

# trends 데이터 2016년 제외
trends = trends[~trends['Date'].str.contains('2016')]

# sales 데이터 month 숫자로 변경
months = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,
          'October':10,'November':11,'December':12}
for month in months:
    idx_list = sales[sales['Month']==month].index.tolist()
    sales.at[idx_list,'Month'] = months[month]

# sales 데이터에서 필요한 column 추출
sales = sales[['Year', 'Month', 'Net']]
sales_by_month = sales.groupby(by=['Year','Month'], as_index=False).sum()
# sales_by_month 2020-4 데이터 없어서 추가
sales_by_month.loc[38.5] = [2020, 4, 0]
sales_by_month = sales_by_month.sort_index().reset_index(drop=True)

# sales 데이터 min-max scaling by month
net_max = sales_by_month['Net'].max()
net_min = sales_by_month['Net'].min()
denominator = net_max - net_min
sales_by_month['Net_MinMax'] = (sales_by_month['Net'] - net_min) / denominator
# print(sales_by_month)

# plot
date_list = []
for date in trends['Date']:
    date = str(date).split('-')
    date_list.append(date[0]+'-'+date[1])

plt.figure(figsize=(15,8))
plt.title('Monthly Google Trend and Sales Trend', fontsize=20)
plt.plot(date_list, trends['Min-Max'], label='Google Trends')
plt.plot(date_list, sales_by_month['Net_MinMax'], label='Sales Trends')
plt.legend()
plt.xticks(rotation=90)
plt.savefig('../../resource/Plot/Google Trends And Sales Trend (Monthly).png')
# plt.show()

# CSV
data = {
    'x': date_list,
    'Google trends': list(trends['Min-Max']),
    'Sales trend': list(sales_by_month['Net_MinMax'])
}
data_csv = pd.DataFrame(data)
data_csv.to_csv('../../resource/PlotCSV/Google Trends And Sales Trend (Monthly).csv', index=False)

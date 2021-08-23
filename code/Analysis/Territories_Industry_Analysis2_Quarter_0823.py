import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv('../../resource/SalesData/Whole Revenue_fillTerritory.csv')

# sales 데이터 month 숫자로 변경
months = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,
          'October':10,'November':11,'December':12}
for month in months:
    idx_list = sales[sales['Month']==month].index.tolist()
    sales.at[idx_list,'Month'] = months[month]

years = range(2017, 2022)
months = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

# 1-2. Quarterly Territory별 총 Sales/거래개수
terri_list = list(sales['Region'].unique())
print(terri_list)
for terri in terri_list:
    df = sales[sales['Region']==terri]
    terri_dict = {}
    for year in years:
        for i, month in enumerate(months):
            key = str(year) + '-' + str(i+1) + 'Q'
            df_date = df[(df['Year'] == year) & (df['Month'].isin(month))]
            if not df_date.empty and df_date['Net'].sum() != 0:
                avg_sales = df_date['Net'].sum() / len(df_date)
                terri_dict[key] = avg_sales
            else:  # 해당 month 데이터 존재하지않음
                terri_dict[key] = 0
    del terri_dict['2021-4Q']
    # print(terri,':',terri_dict)
    # Plot
    plt.figure(figsize=(15, 8))
    title = 'Monthly Average Sales By Territories ' + terri + ' (2017-2021)'
    plt.title(title, fontsize=20)
    plt.plot(list(terri_dict.keys()), list(terri_dict.values()))
    plt.xticks(rotation=90)
    plt.ylabel('Average Sales', fontsize=12)
    # plt.show()
    save_dir = '../../resource/Plot_Quarter/' + title
    plt.savefig(save_dir + '.png')
    # # CSV
    save_dir = '../../resource/PlotCSV_Quarter/' + title
    data = pd.DataFrame(list(terri_dict.items()), columns=['x', 'y'])
    data.to_csv(save_dir + '.csv', index=False)

# 2-2. Quarterly Industry 총 Sales/거래개수
industry_list = [['Hospital','Clinic','Fitness'],['Academic','Private Enterprise','Hotel'],
              ['Others_Others Corporate','Public Association','Others_Aesthetic'],
              ['Military','Others_Individual','Others_etc']]

sales = sales[['Year', 'Month', 'Industry Fin', 'Net']]
for industry in industry_list:
    df1 = sales[sales['Industry Fin'] == industry[0]]
    df2 = sales[sales['Industry Fin'] == industry[1]]
    df3 = sales[sales['Industry Fin'] == industry[2]]
    ids1, ids2, ids3 = {}, {}, {}
    for year in years:
        for i, month in enumerate(months):
            key = str(year) + '-' + str(i+1) + 'Q'

            df_industry1 = df1[(df1['Year'] == year) & (df1['Month'].isin(month))]
            if not df_industry1.empty:
                avg_sales = df_industry1['Net'].sum() / len(df_industry1)
                ids1[key] = avg_sales
            else:  # 해당 month 데이터 존재하지않음
                ids1[key] = 0

            df_industry2 = df2[(df2['Year'] == year) & (df2['Month'].isin(month))]
            if not df_industry2.empty:
                avg_sales = df_industry2['Net'].sum() / len(df_industry2)
                ids2[key] = avg_sales
            else:  # 해당 month 데이터 존재하지않음
                ids2[key] = 0

            df_industry3 = df3[(df3['Year'] == year) & (df3['Month'].isin(month))]
            if not df_industry3.empty:
                avg_sales = df_industry3['Net'].sum() / len(df_industry3)
                ids3[key] = avg_sales
            else:  # 해당 month 데이터 존재하지않음
                ids3[key] = 0
    del ids1['2021-4Q']
    del ids2['2021-4Q']
    del ids3['2021-4Q']
    # Plot
    fig = plt.figure(figsize=(15, 8))  ## 캔버스 생성
    fig.set_facecolor('white')  ## 캔버스 색상 설정
    ax = fig.add_subplot()  ## 그림 뼈대(프레임) 생성

    ax.plot(list(ids1.keys()), list(ids1.values()), label=industry[0])  ## 선그래프 생성
    ax.plot(list(ids1.keys()), list(ids2.values()), label=industry[1])
    ax.plot(list(ids1.keys()), list(ids3.values()), label=industry[2])
    ax.legend()  ## 범례

    name = industry[0] + ', ' + industry[1] + ', ' + industry[2]
    title = 'Monthly Average Sales By Industry ' + name + ' (2017-2021)'
    plt.title(title, fontsize=20)
    plt.xticks(rotation=90)
    plt.ylabel('Average Sales', fontsize=12)
    save_dir = '../../resource/Plot_Quarter/' + title
    plt.savefig(save_dir + '.png')
    # plt.show()
    # CSV
    data = {
        'x': list(ids1.keys()),
        industry[0]: list(ids1.values()),
        industry[1]: list(ids2.values()),
        industry[2]: list(ids3.values())
    }
    data_csv = pd.DataFrame(data)
    save_dir = '../../resource/PlotCSV_Quarter/' + title
    data_csv.to_csv(save_dir+'.csv', index=False)


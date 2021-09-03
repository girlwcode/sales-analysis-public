import pandas as pd

csv_dir = '../../resource/PlotCSV/'
terri_list = ['East', 'West 1', 'West 2', 'South', 'North', 'Overseas', 'Amazon']


# 9. Monthly Average Sales by Industry (4)
data1 = pd.read_csv(csv_dir + 'Monthly Average Sales By Industry Hospital, Clinic, Fitness (2017-2021).csv')
data2 = pd.read_csv(
    csv_dir + 'Monthly Average Sales By Industry Others_Others Corporate, Public Association, Others_Aesthetic (2017-2021).csv')
data3 = pd.read_csv(csv_dir + 'Monthly Average Sales By Industry Academic, Private Enterprise, Hotel (2017-2021).csv')
data4 = pd.read_csv(
    csv_dir + 'Monthly Average Sales By Industry Military, Others_Individual, Others_etc (2017-2021).csv')
data_list = [data1, data2, data3, data4]

print('이 그래프는 2017년 1월부터 2021년 7월까지의 Sales Report 데이터를 활용했습니다.\n'
      '한달 간 산업군별로 한 거래당 평균 매출을 나타냅니다. (Average Sales per Deal = Total Sales/Number of Deals)\n')

max_avg_sales = 0
min_avg_sales = 10000000
max_industry, min_industry = '', ''
for data in data_list:
    for industry in data.columns:
        if industry != 'x':
            df = data[data[industry] > 0]
            month_count = len(df)
            avg_sales = df[industry].sum() / month_count
            # max, min 구하기
            if avg_sales > max_avg_sales:
                max_industry = industry
                max_avg_sales = avg_sales
            if avg_sales < min_avg_sales:
                min_industry = industry
                min_avg_sales = avg_sales
            print(
                f'전체 기간동안 {industry} 산업군이 수익을 낸 달은 {month_count}개월이며, 한 거래당 평균적으로 {round(avg_sales, 2)}루피의 매출을 내고 있습니다.')
    print('')

print(f'한 거래당 평균 매출이 가장 높은 곳은 {max_industry} 산업군이고 가장 낮은 곳은 {min_industry} 산업군입니다.\n')


# 11. Monthly Deal Success Rate By Industry (4)
data1 = pd.read_csv(csv_dir + 'Monthly Deal Success Rate By Industry Hospital, Clinic, Fitness (2017-2021).csv')
data2 = pd.read_csv(
    csv_dir + 'Monthly Deal Success Rate By Industry Others_Others Corporate, Public Association, Others_Aesthetic (2017-2021).csv')
data3 = pd.read_csv(
    csv_dir + 'Monthly Deal Success Rate By Industry Academic, Private Enterprise, Hotel (2017-2021).csv')
data4 = pd.read_csv(
    csv_dir + 'Monthly Deal Success Rate By Industry Military, Others_Individual, Others_etc (2017-2021).csv')
data_list = [data1, data2, data3, data4]

print('이 그래프는 2017년 1월부터 2021년 7월까지의 Potentials 데이터를 활용했습니다.\n'
      '한달 간 산업군별로 Deal의 거래가 완료가 되는 비율을 나타냅니다. (Deal Success Rate = Number of Closed Deals/Number of Deals)\n')

max_avg_rate = 0
min_avg_rate = 2
max_industry, min_industry = '', ''
for data in data_list:
    for industry in data.columns:
        if industry != 'x':
            df = data[data[industry] > 0]
            month_count = len(df)
            avg_rate = df[industry].sum() / month_count
            # max, min 구하기
            if avg_rate > max_avg_rate:
                max_industry = industry
                max_avg_rate = avg_rate
            if avg_rate < min_avg_rate:
                min_industry = industry
                min_avg_rate = avg_rate
            print(f'전체 기간동안 {industry} 산업군은 한 건의 Deal이 평균적으로 {round(avg_rate, 2)}정도의 성사 비율을 보입니다.')
    print('')

print(f'Deal의 월별 평균 성공률이 가장 높은 곳은 {max_industry} 산업군이고 가장 낮은 곳은 {min_industry} 산업군입니다.\n')


# 13. Monthly Average Sales by Territory (7)
data1 = pd.read_csv(csv_dir + 'Monthly Average Sales By Territories East (2017-2021).csv')
data2 = pd.read_csv(csv_dir + 'Monthly Average Sales By Territories West 1 (2017-2021).csv')
data3 = pd.read_csv(csv_dir + 'Monthly Average Sales By Territories West 2 (2017-2021).csv')
data4 = pd.read_csv(csv_dir + 'Monthly Average Sales By Territories South (2017-2021).csv')
data5 = pd.read_csv(csv_dir + 'Monthly Average Sales By Territories North (2017-2021).csv')
data6 = pd.read_csv(csv_dir + 'Monthly Average Sales By Territories Overseas (2017-2021).csv')
data7 = pd.read_csv(csv_dir + 'Monthly Average Sales By Territories Amazon (2017-2021).csv')
data_list = [data1, data2, data3, data4, data5, data6, data7]

print('이 그래프는 2017년 1월부터 2021년 7월까지의 Sales Report 데이터를 활용했습니다.\n'
      '한달 간 지역별로 한 거래당 평균 매출을 나타냅니다. (Average Sales per Deal = Total Sales/Number of Deals)\n')

max_avg_sales = 0
min_avg_sales = 100000000
max_terri, min_terri = '', ''
for i, data in enumerate(data_list):
    df = data[data['y'] > 0]
    month_count = len(df)
    avg_sales = df['y'].sum() / month_count
    # max, min 구하기
    if avg_sales > max_avg_sales:
        max_terri = terri_list[i]
        max_avg_sales = avg_sales
    if avg_sales < min_avg_sales:
        min_terri = terri_list[i]
        min_avg_sales = avg_sales
    # 코로나 이전, 이후 구하기
    covid_before = df[df['x'].str.contains('2017|2018|2019')]['y'].sum() / 36
    covid_after = df[df['x'].str.contains('2020|2021')]['y'].sum() / 19
    before_after = round(covid_after / covid_before, 2)
    print(f'전체 기간동안 {terri_list[i]} 지역이 수익을 낸 달은 {month_count}개월이며, 한 거래당 평균적으로 {round(avg_sales, 2)}루피의 매출을 내고 있습니다.')
    print(f'Covid19이전에는 평균적으로 {round(covid_before,2)}루피의 매출을, '
          f'Covid19가 발생한 2020년 1월 이후에는 평균적으로 {round(covid_after,2)}루피의 매출을 냈습니다. Covid19 전후 약 {before_after}배 차이를 보입니다.')

print('')
print(f'한 거래당 평균 매출이 가장 높은 곳은 {max_terri} 지역이며 가장 낮은 곳은 {min_terri} 지역입니다.\n')


# 14. Monthly Deal Success Rate By Territory (7)
data1 = pd.read_csv(csv_dir + 'Monthly Deal Success Rate By Territories East (2017-2021).csv')
data2 = pd.read_csv(csv_dir + 'Monthly Deal Success Rate By Territories West1 (2017-2021).csv')
data3 = pd.read_csv(csv_dir + 'Monthly Deal Success Rate By Territories West 2 (2017-2021).csv')
data4 = pd.read_csv(csv_dir + 'Monthly Deal Success Rate By Territories South (2017-2021).csv')
data5 = pd.read_csv(csv_dir + 'Monthly Deal Success Rate By Territories North (2017-2021).csv')
data6 = pd.read_csv(csv_dir + 'Monthly Deal Success Rate By Territories Overseas (2017-2021).csv')
data7 = pd.read_csv(csv_dir + 'Monthly Deal Success Rate By Territories Amazon (2017-2021).csv')
data_list = [data1, data2, data3, data4, data5, data6, data7]

print('이 그래프는 2017년 1월부터 2021년 7월까지의 Potentials 데이터를 활용했습니다.\n'
      '한달 간 지역별로 Deal의 거래가 완료가 되는 비율을 나타냅니다. (Deal Success Rate = Number of Closed Deals/Number of Deals)\n')

max_avg_rate = 0
min_avg_rate = 2
max_terri, min_terri = '', ''
for i, data in enumerate(data_list):
    df = data[data['y'] > 0]
    month_count = len(df)
    avg_rate = df['y'].sum() / month_count
    # max, min 구하기
    if avg_rate > max_avg_rate:
        max_terri = terri_list[i]
        max_avg_rate = avg_rate
    if avg_rate < min_avg_rate:
        min_terri = terri_list[i]
        min_avg_rate = avg_rate
    # 코로나 이전, 이후 구하기 (Amazon 제외)
    if i != 6:
        covid_before = df[df['x'].str.contains('2017|2018|2019')]['y'].sum() / 36
        covid_after = df[df['x'].str.contains('2020|2021')]['y'].sum() / 19
        before_after = round(covid_after / covid_before, 2)
    print(f'전체 기간동안 {terri_list[i]} 지역은 한 건의 Deal이 평균적으로 {round(avg_rate, 2)}정도의 성사 비율을 보입니다.')
    if i != 6: # 아마존 제외
        print(f'Covid19이전에는 평균적으로 {round(covid_before, 2)}정도의 성사 비율을, '
              f'Covid19가 발생한 2020년 1월 이후에는 평균적으로 {round(covid_after, 2)}정도의 성사 비율을 보입니다. Covid19 전후 약 {before_after}배 차이를 보입니다.')

print('')
print(f'Deal의 월별 평균 성공률이 가장 높은 곳은 {max_terri} 지역이고 가장 낮은 곳은 {min_terri} 지역입니다.')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

deal = pd.read_csv('../../resource/CleansedData/ZohoCRM/Potentials_001_fillIndustry.csv')
ss_full = pd.read_csv('../../resource/PlotCSV/Monthly Sales Success Rate By Industry Hospital, Clinic, Fitness (2017-2021).csv')

# Territory별 industry(clinic, hospital, fitness)의 성장 가능성
terri_list = ['East', 'West 1', 'West 2', 'South', 'North']
industry_list = ['Clinic', 'Hospital', 'Fitness']

# 1. Territory별 industry의 Deal 분포
dealNum_east = pd.read_csv('../../resource/PlotCSV/Deal of Industry by territories East.csv')
dealNum_w1 = pd.read_csv('../../resource/PlotCSV/Deal of Industry by territories West 1.csv')
dealNum_w2 = pd.read_csv('../../resource/PlotCSV/Deal of Industry by territories West 2.csv')
dealNum_south = pd.read_csv('../../resource/PlotCSV/Deal of Industry by territories South.csv')
dealNum_north = pd.read_csv('../../resource/PlotCSV/Deal of Industry by territories North.csv')
dealNum_df_list = [dealNum_east, dealNum_w1, dealNum_w2, dealNum_south, dealNum_north]

# 2. Territory별 Deal Success Rate
ds_terri_dict = dict.fromkeys(terri_list)

for terri in terri_list:
    dealNum_full = len(deal[deal['Territory_fin']==terri])
    dealNum_closed = len(deal[(deal['Territory_fin']==terri) & (deal['Stage'].str.contains('5|6|7'))])
    ds_terri_dict[terri] = dealNum_closed / dealNum_full

# print(ds_terri_dict)

# 3. Industry별 Deal Success Rate
ds_industry_dict = dict.fromkeys(industry_list)

for industry in industry_list:
    dealNum_full = len(deal[deal['Industry Fin']==industry])
    dealNum_closed = len(deal[(deal['Industry Fin']==industry) & (deal['Stage'].str.contains('5|6|7'))])
    ds_industry_dict[industry] = dealNum_closed / dealNum_full
# print(ds_industry_dict)

# 4. Industry별 Sales Success Rate: Monthly Max - Min(0제외)
ss_industry_dict = dict.fromkeys(industry_list)

ss_full = ss_full.replace(0, np.nan)
for industry in industry_list:
    ss_industry_dict[industry] = (ss_full[industry].max() - ss_full[industry].min()) / 100
# print(ss_industry_dict)

# 5. Google Map 크롤링 결과 Territory 별 industry 분포 비율
google_clinic = pd.read_csv('../../resource/GeocodingData/merge/Clinic_final2.csv')
google_hos = pd.read_csv('../../resource/GeocodingData/merge/Hospital_final2.csv')
google_fit = pd.read_csv('../../resource/GeocodingData/merge/Fitness_final2.csv')

google_terri_dict = dict.fromkeys(terri_list)
for terri in terri_list:
    clinic_num = len(google_clinic[google_clinic['Territory'] == terri])
    hos_num = len(google_hos[google_hos['Territory'] == terri])
    fit_num = len(google_fit[google_fit['Territory'] == terri])
    sum = clinic_num + hos_num + fit_num
    google_terri_dict[terri] = [clinic_num / sum, hos_num / sum, fit_num / sum]


# 점수 내기
for i, terri in enumerate(terri_list):
    full_df = pd.DataFrame()
    full_df['x'] = industry_list
    score_list = []
    deal_success_terri = ds_terri_dict[terri]
    google_industry_list = google_terri_dict[terri]

    df = dealNum_df_list[i]
    for j, industry in enumerate(industry_list):
        df_industry = df[df['x']==industry].reset_index(drop=True)
        deal_distribution = df_industry.at[0,'Deal'] / df['Deal'].sum()

        score = deal_distribution * deal_success_terri * ds_industry_dict[industry] * ss_industry_dict[industry] * google_industry_list[j]
        score_list.append(score * 100)
    # print(score_list)
    full_df['y'] = score_list
    title = 'Google Insight by Territory ' + terri
    plt.title(title)
    plt.bar(industry_list, score_list)
    plt.savefig('../../resource/Plot/'+title+'.png')
    # plt.show()
    full_df.to_csv('../../resource/Score/'+title+'.csv', index=False)
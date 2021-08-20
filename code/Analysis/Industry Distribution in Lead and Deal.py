import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

####1-1
lead =pd.read_csv(r"C:\Users\Lenovo\PycharmProjects\new_cleansing\resource\CleansedData\ZohoCRM\Leads_001_IndustryCleansed.csv")
deal = pd.read_csv(r"C:\Users\Lenovo\PycharmProjects\new_cleansing\resource\CleansedData\ZohoCRM\Potentials_001_fillIndustry.csv")
#
# x_list = ['Fitness', 'Hospital', 'Clinic',  'Academic', 'Hotel','Military','Public Association', 'Private Enterprise',  'Others_Aesthetic',
#           'Others_Others Corporate',  'Others_Individual',  'Others_etc' ]
# #리드 딕셔너리
# industry = list(lead['Industry Fin'].unique())
# lead_dict = {string : 0 for string in x_list}
# for ind in lead['Industry Fin']:
#      if ind in industry:
#         lead_dict[ind]+=1
# lead_dict
# # 딜 딕셔너리
# industry = list(deal['Industry Fin'].unique())
# deal_dict = {string : 0 for string in x_list}
# for ind in deal['Industry Fin']:
#      if ind in industry:
#         deal_dict[ind]+=1
# deal_dict
#
# plt.figure(figsize=(15, 8))
# title = 'Distribution of Industry in Lead and Deal Data'
# plt.title(title, fontsize=20)
#
# plt.bar(x_list, list(lead_dict.values()) , color='green', label = 'Lead')
# plt.bar(x_list, list(deal_dict.values()), color = 'red', bottom = np.array( list(lead_dict.values()) ), label = 'Deal')
# plt.legend()
# plt.xticks(rotation = 90)
# plt.ylabel('Counts', fontsize=12)
#
# save_dir = r'../../resource/Plot'
# saveT = '/lead and deal by industry Bar.png'
# plt.savefig(save_dir + saveT)
#
# #csv 만들기
# data={
#     'x':list(x_list),
#     'Lead': list(lead_dict.values()),
#     'Deal': list(deal_dict.values())
# }
#
#
# ld_df = pd.DataFrame(data)
# save_dir = r'C:\Users\Lenovo\PycharmProjects\new_cleansing\resource\PlotCSV'
# saveT = '\lead and deal by industry.csv'
# ld_df.to_csv(save_dir + saveT, index = False)



####1-2
DD =deal[['Industry Fin', 'Territory_fin']]
terrList = DD['Territory_fin'].unique()
# terrList[6] = 'Amazon&CS'
for terr in terrList:
    df = DD[DD['Territory_fin'] == terr]
    indList = df['Industry Fin'].unique()
    dict_ind = {string: 0 for string in indList}
    for ind in df['Industry Fin']:
        if ind in dict_ind.keys():
            dict_ind[ind] += 1
    plt.figure(figsize=(15, 8))
    title = 'Distribution of Industry in Deal Territory: ' + terr
    plt.title(title, fontsize=20)
    a = list(dict_ind.keys())
    b = list(dict_ind.values())
    plt.bar(a, b)
    plt.xticks(rotation=90)
    plt.ylabel('Counts', fontsize=12)
    save_dir = r'../../resource/Plot'
    saveT = ('/Distribution of Industry '+terr+'.png')
    plt.savefig(save_dir + saveT)



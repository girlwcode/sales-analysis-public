import pandas as pd

origin_data_path = '../resource/OriginalData/'
file_name = 'Accounts_001'
leads = pd.read_csv(origin_data_path+file_name+'.csv')

save_col_path = '../resource/SaveCol/'
txt_name = 'Account_save_col.txt'

leads_col = pd.read_csv(save_col_path+txt_name, sep='\t')

print(leads_col)

# # Use this If, there's a outlier in drop col txt
# leads_col = leads_col.drop(columns=['Unnamed: 1','Unnamed: 4','Unnamed: 67'])
leads_col = leads_col.columns.tolist()

leads2 = leads[leads_col]
outputFileName = file_name+'_droppedCol.csv'
leads2.to_csv('../resource/CleansedData/ParsedData/'+outputFileName, index=False)
print(leads2.shape)
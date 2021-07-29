import pandas as pd

origin_data_path = '../resource/OriginalData/'
file_name = ''
leads = pd.read_csv(origin_data_path+file_name)

drop_col_path = '../resource/DropCol'
txt_name = ''

leads_col = pd.read_csv(drop_col_path+txt_name, sep='\t')

# Use this If, there's a outlier in drop col txt
leads_col = leads_col.drop(columns=['Unnamed: 1','Unnamed: 4','Unnamed: 67'])
leads_col = leads_col.columns.tolist()
print(leads_col)

leads2 = leads[leads_col]
outputFileName = file_name+'_droppedCol.csv'
leads2.to_csv(outputFileName)
print(leads2.shape)
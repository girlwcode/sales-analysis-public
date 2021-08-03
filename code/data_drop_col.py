import pandas as pd

# use this if dataset is in original directory
# origin_data_path = '../resource/OriginalData/'
# file_name = 'Potentials_001'
# leads = pd.read_csv(origin_data_path+file_name+'.csv')

# use this if dataset is in modified directory
# Contacts - Contacts_001_unsubscribed_row_deleted
# Potentials - Potentials_001_USDtoINR
modified_data_path = '../resource/CleansedData/ModifiedData/'
file_name = 'Potentials_001_USDtoINR'
leads = pd.read_csv(modified_data_path+file_name+'.csv')
file_name = 'Potentials_001'


save_col_path = '../resource/SaveCol/'
txt_name = 'Potentials_save_col.txt'

leads_col = pd.read_csv(save_col_path+txt_name, sep='\t')

print(leads_col)

# Use this If, there's a outlier in drop col txt (Contacts)
#leads_col = leads_col.drop(columns=['Unnamed: 26'])

leads_col = leads_col.columns.tolist()

leads2 = leads[leads_col]
outputFileName = file_name+'_droppedCol.csv'
leads2.to_csv('../resource/CleansedData/ParsedData/'+outputFileName, index=False)
print(leads2.shape)
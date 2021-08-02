#
import pandas as pd
leads = pd.read_csv('../resource/OriginalData/Leads_001.csv')
leads['Unsubscribed Mode']
leads['Unsubscribed Time']
for i in range(10691):
    if leads['Unsubscribed Mode'][i]=='Manual':
        del leads['Unsubscribed Mode'][i]

leads.to_csv('../resource/CleansedData/ModifiedData/Leads_001_manual_row_deleted.csv')
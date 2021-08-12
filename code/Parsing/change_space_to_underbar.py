import pandas as pd
def change_space_to_name():#pandas 객체를 리턴함
    target_path= '../../resource/CRM_OriginalData/'
    target_file='Accounts_001'
    accounts=pd.read_csv(target_path+target_file+'.csv')
    accounts.rename(columns = lambda x: x.replace(' ','_'), inplace = True)
    res=accounts
    return  res
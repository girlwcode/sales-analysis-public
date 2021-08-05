# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
import pandas as pd
import re


#70개의 한국어 사업장 제거됨
path= '../../resource/CleansedData/ParsedData/'
file_name='Contacts_001_droppedCol'
csv=pd.read_csv(path+file_name+'.csv')
save_as='../resource/CleansedData/ModifiedData/Contacts_001_deleted_korean.csv'


csv['Full Name']


cnt=0
for row in csv['Full Name']:
    if row.isascii()==False:
        print(row)
        cnt+=1
print(cnt)


cnt=0
for i in range(len(csv['Full Name'])):
    hangul=re.compile('[ㄱ-ㅎ|가-힣]+')
    name=hangul.findall(csv['Full Name'][i]) 
    if len(name)!=0:
        csv=csv.drop(i)
        cnt+=1
print(cnt)           


csv['Full Name']


#한국말 있는지 확인
korean=[]
for row in csv['Full Name']:
    hangul=re.compile('[ㄱ-ㅎ|가-힣]+')
    #print(hangul.findall(row))
    name=hangul.findall(row)
    if len(name)!=0:
        korean.append(name)
korean

csv.to_csv(save_as,index=False)



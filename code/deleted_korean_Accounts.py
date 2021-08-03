import pandas as pd
import re

#44개의 한국어 사업장 제거됨
path='../resource/CleansedData/ParsedData/'
file_name='Accounts_001_droppedCol'
csv=pd.read_csv(path+file_name+'.csv')
save_as='../resource/CleansedData/ModifiedData/Accounts_001_deleted_korean.csv'


csv['Company Name']


cnt=0
for row in csv['Company Name']:
    if row.isascii()==False:
        print(row)
        cnt+=1
print(cnt)


cnt=0
for i in range(len(csv['Company Name'])):
    hangul=re.compile('[ㄱ-ㅎ|가-힣]+')
    name=hangul.findall(csv['Company Name'][i]) 
    if len(name)!=0:
        csv=csv.drop(i)
        cnt+=1
print(cnt)           


csv['Company Name']

csv.to_csv(save_as,index=False)
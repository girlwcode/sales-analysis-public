import pandas as pd
from openpyxl import Workbook

##Sales Person - Owner Id로 채워주기
# zcrm_1920545000000117001 == Arun Sharma
# zcrm_1920545000001530001 == Mahesh Gulwani
# zcrm_1920545000011182001 == Taukheer Ahmed

# wb = openpyxl.Workbook("../code/Accounts/Accounts_001_droppedCol2.csv")
# ws = wb.active
# wb.save(accounts)
# def fill_SalesPerson():
#     for row in ws['AC']:
#         for cell in row:
#             if cell == 'zcrm_1920545000000117001':
#                 cell.append('Arun Sharma')
#     wb.save("Accounts_001_droppedCol2")
#
dfs = pd.read_csv("../../resource/CleansedData/ParsedData/Accounts_001_droppedCol.csv")

num = 0
for df in dfs['Company Owner ID'] :
    num += 1
    if df == 'zcrm_1920545000000117001' :
        dfs['Sales Person'][num] = 'Arun Sharma'

# df[(df['Company Owner ID']=='zcrm_1920545000000117001')]['Sales person'] ='Arun Sharma'
# print(df)

dfs.to_csv('Accounts_001_droppedCol2.csv',index =False)
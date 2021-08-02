import pandas as pd
from openpyxl import Workbook

##Sales Person - Owner Id로 채워주기
# zcrm_1920545000000117001 == Arun Sharma
# zcrm_1920545000001530001 == Mahesh Gulwani
# zcrm_1920545000011182001 == Taukheer Ahmed
# zcrm_1920545000000243011 ==Karn Sharma
# zcrm_1920545000000097003 == Karn Sharma
# zcrm_1920545000000097003 == Anees Mukhtar ==zcrm_1920545000001670001

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

for i in dfs.index :
    if dfs['Company Owner ID'][i] == 'zcrm_1920545000000117001':
        dfs['Sales Person'][i] = 'Arun Sharma'
    if dfs['Company Owner ID'][i] == 'zcrm_1920545000001530001':
        dfs['Sales Person'][i] = 'Mahesh Gulwani'
    if dfs['Company Owner ID'][i] == 'zcrm_1920545000011182001':
        dfs['Sales Person'][i] = 'Taukheer Ahmed'
    if dfs['Company Owner ID'][i] == 'zcrm_1920545000000243011':
        dfs['Sales Person'][i] = 'Karn Sharma'
    if dfs['Company Owner ID'][i] == 'zcrm_1920545000001670001':
        dfs['Sales Person'][i] = 'Anees Mukhtar'

dfs = dfs.to_csv("Accounts.csv")


import pandas as pd

accounts = pd.read_csv('../resource/CleansedData/ParsedData/Accounts_001_droppedCol.csv')
print(accounts['Ownership'][3])
print(accounts['Ownership'].value_counts())


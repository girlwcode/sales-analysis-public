import pandas as pd

accounts = pd.read_csv('../../resource/CleansedData/ParsedData/Accounts_001_droppedCol.csv')
print(accounts['Ownership'].value_counts())

def ownership(accounts) :
    for account in accounts['Ownership'] :
        if str(account).startswith('Public'):
            account = "Public"

ownership(accounts)
print(accounts['Ownership'].value_counts())

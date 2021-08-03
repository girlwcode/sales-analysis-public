import pandas as pd

# Industry Cleansing
accounts = pd.read_csv('../resource/CleansedData/Accounts_001_fillTerritories_final.csv')
deal = pd.read_csv('../resource/CleansedData/ParsedData/Potentials_001_droppedCol.csv')

print(deal.columns)
#'Industry', 'Sub industry'
#print(accounts.columns)

# 34개, ['Hospitality' 'Fitness' 'Government Medical' 'Health Center' 'Others'
#  'Sport team' 'Public Medical' 'Individual Fitness' 'Dealer_FItness'
#  'Defense' 'Enterprise' 'University' 'Hotel' 'Dealer' 'Private Medical'
#  'National and Public Institutions' 'Military base'
#  'Health Functional Food sales' 'Key man' 'Public Health Center' 'Sports'
#  'Dealer_Medical' 'Pharmacy' 'High budget Fitness' 'Middle budget Fitness'
#  'Individual' 'Diagnostic center' 'Spa' 'Corporate wellness' 'Corporates'
#  'Academic' 'Hospitals' 'Amazon/CS' 'Aarti Diagnostic Centre']
#print(accounts['Industry'].nunique(), accounts['Industry'].unique())

print(accounts['Industry'].isnull().sum())
<<<<<<< HEAD
# 1433개
=======
>>>>>>> origin/master

import pandas as pd
import os

google_dir = '../../resource/GeocodingData/merge/'
sales_dir = '../../resource/SalesData/'

# installed data 삭제
installed = pd.read_csv(sales_dir + 'Installation_full.csv')
clients = installed['Client'].values.tolist()
clients = [x.lower() for x in clients]

# fitness
un_fitness = pd.read_csv(google_dir + 'Fitness.csv')
fit_clients = ['Anytime Fitness', 'Golds Gym', "Gold's Gym", 'Kris Gethin', 'MCA', 'Pullela Gopichand Academy',
               'Snap Fitness', 'Slam Fitness', 'Apple Fitness', 'Nittro Gym', 'Twalkar Brothers Pvt Ltd', 'K11 Academy',
               'Chisel', 'One Above', 'UFC GYM']
fit_clients = [x.lower() for x in fit_clients]

print(len(un_fitness), end='\t\t')  # 5360
for client in fit_clients:
    drop_idx = un_fitness[un_fitness['Company_Name'].str.lower().str.contains(client)].index.tolist()
    un_fitness = un_fitness.drop(drop_idx)

for client in clients:
    try:
        drop_idx = un_fitness[un_fitness['Company_Name'].str.lower().str.contains(client)].index.tolist()
        un_fitness = un_fitness.drop(drop_idx)
    except: continue
print(len(un_fitness))  # 4834

# hospital
un_hos = pd.read_csv(google_dir + 'Hospital.csv')
hos_cli_clients = ['AIIMS', 'Guru Teg Bahadur Hospital', "King George's Medical University, Lucknow",
                  'Apollo Hospital', 'Greater Kailash Hospital', 'Sakra World Hospital', 'Manipal University',
                  'Max Health Care', 'Dr. Ram Manohar', 'Global Hospital', 'The Madras Medical Mission',
                  'Ratandeep Advance Care', 'Asian Bariatrics', 'Dr Tulip Obesity Center',
                  'Vikram Hospital', 'Motwani Health Care', 'Jammu Hospital', 'Nidhi Hospital', 'Jupiter Hospital',
                  'RG Urology & Laparoscopy Hospital', 'IndoGulf Hospital', 'VLCC', 'Vibes Healthcare Pvt Ltd',
                  'Oliva Clinic', 'V Care', 'Perfect Wellness', 'Bodycraft Salon Skin & Cosmetology Private Limited',
                  'Alm Ayush', 'Roundglass Wellbeing Private Limited', 'visit']
hos_cli_clients = [x.lower() for x in hos_cli_clients]

print(len(un_hos), end='\t\t')  # 5710
for client in hos_cli_clients:
    drop_idx = un_hos[un_hos['Company_Name'].str.lower().str.contains(client)].index.tolist()
    un_hos = un_hos.drop(drop_idx)

for client in clients:
    try:
        drop_idx = un_hos[un_hos['Company_Name'].str.lower().str.contains(client)].index.tolist()
        un_hos = un_hos.drop(drop_idx)
    except: continue
print(len(un_hos))  # 5402

# clinic
un_cli = pd.read_csv(google_dir + 'Clinic.csv')

print(len(un_cli), end='\t\t')  # 5628
for client in hos_cli_clients:
    drop_idx = un_cli[un_cli['Company_Name'].str.lower().str.contains(client)].index.tolist()
    un_cli = un_cli.drop(drop_idx)

for client in clients:
    try:
        drop_idx = un_cli[un_cli['Company_Name'].str.lower().str.contains(client)].index.tolist()
        un_cli = un_cli.drop(drop_idx)
    except: continue
print(len(un_cli))  # 5285

un_fitness.to_csv(google_dir+'Fitness_final.csv', index=False)
un_hos.to_csv(google_dir+'Hospital_final.csv', index=False)
un_cli.to_csv(google_dir+'Clinic_final.csv', index=False)
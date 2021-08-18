import csv
import os

trends_dir = '../../resource/GoogleTrends/Origin/'
details = ['2016/', '2017/', '2018/', '2019/', '2020/', '2021/']

# 데이터 헤더 없애기
month = 1
for csv_data in os.listdir(trends_dir+details[5]):
    f = open(trends_dir+details[5]+csv_data, encoding='utf-8')
    data = csv.reader(f)
    next(data)
    next(data)

    save_dir = '../../resource/GoogleTrends/Parsing/' + details[5] + str(month) + '.csv'
    w = open(save_dir, 'w')
    writer = csv.writer(w)
    writer.writerows(data)
    w.close()
    f.close()
    month+=1
import pandas as pd
import csv
#import matplotlib.pyplot as pt
from itertools import groupby

"""
ลองใช้ggroupbyแยกปีแยกยี่ห้อ

"""

df = pd.read_csv('norway_new_car_sales_by_make.csv')

# data_make = df.groupby('Make')#คำสั่งใช้groupbyแยกยี่ห้อ
data = df.groupby(['Year', 'Make'])#คำสั่งgroupby แยกปีและรุ่น

for i in data:
	print((sum(i['Year']=='2007',i['Make']=='Toyata')).Quantity)
print(sum(data.get_group((2007, 'Toyota')).Quantity))  # บวกยอดขายรถรุ่นToyota ปี 2007 ได้แล้วโว้ยยยย
                                                        # ใน get_group ให้กำหนดปีและรุ่นที่ต้องการ

# data_2007 = df[df.Year == 2007]#เอาแค่ของปี2007






"""
ยอดรวมของรถทุกรุ่นในแต่ละปี ตั้งแต่ 2007-2016 ใช้ไฟล์ .txt

"""

# file = open('norway_new_car_sales_by_make1.txt')
# data = csv.reader(file)
# table = [row for row in data]
# print(table)

# gb = groupby(table, lambda x: x[0])

# for key, group in gb:
#     total = 0
#     for item in group:
#         total += int(item[3])
#     print(item[0], total)



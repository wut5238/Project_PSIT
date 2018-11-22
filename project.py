import pandas as pd
import csv
from itertools import groupby

"""
ลองใช้ggroupbyแยกปีแยกยี่ห้อ

"""

# df = pd.read_csv('norway_new_car_sales_by_make.csv')

# data_make = df.groupby('Make')#คำสั่งใช้groupbyแยกยี่ห้อ
# data_year = df.groupby('Year')#คำสั่งgroupby แยกปี

# # print(data.get_group('Toyota'))
# for k, v in data_make:
#     print(k)
#     print(v)
#data_2007 = df[df.Year == 2007]#เอาแค่ของปี2007


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



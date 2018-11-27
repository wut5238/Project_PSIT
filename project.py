import pandas as pd

"""
Car Sales in Norway Analysis

"""
year = [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]

df = pd.read_csv('norway_new_car_sales_by_make.csv')

#Clean Data

data = df.groupby(['Year', 'Make'])#คำสั่งgroupby แยกปีและรุ่น
df.set_index(['Year'],inplace=True)

# กำหนด column ที่เป็นปีที่กำหนดและยี่ห้อรถในปีนั้น

make_2007 = df.loc[:2007, 'Make']
make_2008 = df.loc[2008:2008, 'Make']
make_2009 = df.loc[2009:2009, 'Make']
make_2010 = df.loc[2010:2010, 'Make']
make_2011 = df.loc[2011:2011, 'Make']
make_2012 = df.loc[2012:2012, 'Make']
make_2013 = df.loc[2013:2013, 'Make']
make_2014 = df.loc[2014:2014, 'Make']
make_2015 = df.loc[2015:2015, 'Make']
make_2016 = df.loc[2016:2016, 'Make']

# find top_10 of each year

def year_2007():
    make = make_2007.unique() # ดึงยี่ห้อรถแต่ละรุ่นในปี 2007
    total = []
    lst = dict() # เก็บจำนวนยอดขายของรถแต่ละรุ่น

    for i in range(len(make)):
        total.append(sum(data.get_group((year[0], make[i])).Quantity))
        if sum(data.get_group((year[0], make[i])).Quantity) not in lst:
            lst[sum(data.get_group((year[0], make[i])).Quantity)] = make[i]
        else:
            pass

    total.sort(reverse=True)
    top_10 = total[0:10]
    top_10_2007 = [(lst[i], i) for i in top_10]
    return top_10_2007

def year_2008():
    make = make_2008.unique() # ดึงยี่ห้อรถแต่ละรุ่นในปี 2008
    total = []
    lst = dict() # เก็บจำนวนยอดขายของรถแต่ละรุ่น

    for i in range(len(make)):
        total.append(sum(data.get_group((year[1], make[i])).Quantity))
        if sum(data.get_group((year[1], make[i])).Quantity) not in lst:
            lst[sum(data.get_group((year[1], make[i])).Quantity)] = make[i]
        else:
            pass

    total.sort(reverse=True)
    top_10 = total[0:10]
    top_10_2008 = [(lst[i], i) for i in top_10]
    return top_10_2008

def year_2009():
    make = make_2009.unique() # ดึงยี่ห้อรถแต่ละรุ่นในปี 2009
    total = []
    lst = dict() # เก็บจำนวนยอดขายของรถแต่ละรุ่น

    for i in range(len(make)):
        total.append(sum(data.get_group((year[2], make[i])).Quantity))
        if sum(data.get_group((year[2], make[i])).Quantity) not in lst:
            lst[sum(data.get_group((year[2], make[i])).Quantity)] = make[i]
        else:
            pass

    total.sort(reverse=True)
    top_10 = total[0:10]
    top_10_2009 = [(lst[i], i) for i in top_10]
    return top_10_2009

def year_2010():
    make = make_2010.unique() # ดึงยี่ห้อรถแต่ละรุ่นในปี 2010
    total = []
    lst = dict() # เก็บจำนวนยอดขายของรถแต่ละรุ่น

    for i in range(len(make)):
        total.append(sum(data.get_group((year[3], make[i])).Quantity))
        if sum(data.get_group((year[3], make[i])).Quantity) not in lst:
            lst[sum(data.get_group((year[3], make[i])).Quantity)] = make[i]
        else:
            pass

    total.sort(reverse=True)
    top_10 = total[0:10]
    top_10_2010 = [(lst[i], i) for i in top_10]
    return top_10_2010

def year_2011():
    make = make_2011.unique() # ดึงยี่ห้อรถแต่ละรุ่นในปี 2011
    total = []
    lst = dict() # เก็บจำนวนยอดขายของรถแต่ละรุ่น

    for i in range(len(make)):
        total.append(sum(data.get_group((year[4], make[i])).Quantity))
        if sum(data.get_group((year[4], make[i])).Quantity) not in lst:
            lst[sum(data.get_group((year[4], make[i])).Quantity)] = make[i]
        else:
            pass

    total.sort(reverse=True)
    top_10 = total[0:10]
    top_10_2011 = [(lst[i], i) for i in top_10]
    return top_10_2011

def year_2012():
    make = make_2012.unique() # ดึงยี่ห้อรถแต่ละรุ่นในปี 2012
    total = []
    lst = dict() # เก็บจำนวนยอดขายของรถแต่ละรุ่น

    for i in range(len(make)):
        total.append(sum(data.get_group((year[5], make[i])).Quantity))
        if sum(data.get_group((year[5], make[i])).Quantity) not in lst:
            lst[sum(data.get_group((year[5], make[i])).Quantity)] = make[i]
        else:
            pass

    total.sort(reverse=True)
    top_10 = total[0:10]
    top_10_2012 = [(lst[i], i) for i in top_10]
    return top_10_2012

def year_2013():
    make = make_2013.unique() # ดึงยี่ห้อรถแต่ละรุ่นในปี 2013
    total = []
    lst = dict() # เก็บจำนวนยอดขายของรถแต่ละรุ่น

    for i in range(len(make)):
        total.append(sum(data.get_group((year[6], make[i])).Quantity))
        if sum(data.get_group((year[6], make[i])).Quantity) not in lst:
            lst[sum(data.get_group((year[6], make[i])).Quantity)] = make[i]
        else:
            pass

    total.sort(reverse=True)
    top_10 = total[0:10]
    top_10_2013 = [(lst[i], i) for i in top_10]
    return top_10_2013

def year_2014():
    make = make_2014.unique() # ดึงยี่ห้อรถแต่ละรุ่นในปี 2014
    total = []
    lst = dict() # เก็บจำนวนยอดขายของรถแต่ละรุ่น

    for i in range(len(make)):
        total.append(sum(data.get_group((year[7], make[i])).Quantity))
        if sum(data.get_group((year[7], make[i])).Quantity) not in lst:
            lst[sum(data.get_group((year[7], make[i])).Quantity)] = make[i]
        else:
            pass

    total.sort(reverse=True)
    top_10 = total[0:10]
    top_10_2014 = [(lst[i], i) for i in top_10]
    return top_10_2014

def year_2015():
    make = make_2015.unique() # ดึงยี่ห้อรถแต่ละรุ่นในปี 2015
    total = []
    lst = dict() # เก็บจำนวนยอดขายของรถแต่ละรุ่น

    for i in range(len(make)):
        total.append(sum(data.get_group((year[8], make[i])).Quantity))
        if sum(data.get_group((year[8], make[i])).Quantity) not in lst:
            lst[sum(data.get_group((year[8], make[i])).Quantity)] = make[i]
        else:
            pass

    total.sort(reverse=True)
    top_10 = total[0:10]
    top_10_2015 = [(lst[i], i) for i in top_10]
    return top_10_2015

def year_2016():
    make = make_2016.unique() # ดึงยี่ห้อรถแต่ละรุ่นในปี 2016
    total = []
    lst = dict() # เก็บจำนวนยอดขายของรถแต่ละรุ่น

    for i in range(len(make)):
        total.append(sum(data.get_group((year[9], make[i])).Quantity))
        if sum(data.get_group((year[9], make[i])).Quantity) not in lst:
            lst[sum(data.get_group((year[9], make[i])).Quantity)] = make[i]
        else:
            pass

    total.sort(reverse=True)
    top_10 = total[0:10]
    top_10_2016 = [(lst[i], i) for i in top_10]
    return top_10_2016

import matplotlib.pyplot as plt #import module สำหรับสร้างกราฟ
import csv
import sys
from matplotlib.ticker import FuncFormatter


csvwriter = csv.writer(open("new.csv", "w+")) 
a = year_2016()
for row in a:
	csvwriter.writerow((row))


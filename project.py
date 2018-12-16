import pandas as pd
import matplotlib.pyplot as plt

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

#plot graph

def allgraph():
    '''เรียกใช้ฟังชั่นพล็อตกราฟของทุกปี'''
    graph_2007()
    graph_2008()
    graph_2009()
    graph_2010()
    graph_2011()
    graph_2012()
    graph_2013()
    graph_2014()
    graph_2015()
    graph_2016()

def graph_2007():
    '''ฟังชั่นพล็อตกราฟท็อป10ปี2007'''
    top_10_2007 = year_2007()
    x_val = [x[0] for x in top_10_2007]
    y_val = [x[1] for x in top_10_2007]
    plt.bar(x_val, y_val, color='red')
    plt.title('Top 10 Year 2007', color='green')
    plt.show()

def graph_2008():
    '''ฟังชั่นพล็อตกราฟท็อป10ปี2008'''
    top_10_2008 = year_2008()
    x_val = [x[0] for x in top_10_2008]
    y_val = [x[1] for x in top_10_2008]
    plt.bar(x_val, y_val, color='red')
    plt.title('Top 10 Year 2008', color='green')
    plt.show()

def graph_2009():
    '''ฟังชั่นพล็อตกราฟท็อป10ปี2009'''
    top_10_2009 = year_2009()
    x_val = [x[0] for x in top_10_2009]
    y_val = [x[1] for x in top_10_2009]
    plt.bar(x_val, y_val, color='red')
    plt.title('Top 10 Year 2009', color='green')
    plt.show()

def graph_2010():
    '''ฟังชั่นพล็อตกราฟท็อป10ปี2010'''
    top_10_2010 = year_2010()
    x_val = [x[0] for x in top_10_2010]
    y_val = [x[1] for x in top_10_2010]
    plt.bar(x_val, y_val, color='red')
    plt.title('Top 10 Year 2010', color='green')
    plt.show()

def graph_2011():
    '''ฟังชั่นพล็อตกราฟท็อป10ปี2011'''
    top_10_2011 = year_2011()
    x_val = [x[0] for x in top_10_2011]
    y_val = [x[1] for x in top_10_2011]
    plt.bar(x_val, y_val, color='red')
    plt.title('Top 10 Year 2011', color='green')
    plt.show()

def graph_2012():
    '''ฟังชั่นพล็อตกราฟท็อป10ปี2012'''
    top_10_2012 = year_2012()
    x_val = [x[0] for x in top_10_2012]
    y_val = [x[1] for x in top_10_2012]
    plt.bar(x_val, y_val, color='red')
    plt.title('Top 10 Year 2012', color='green')
    plt.show()

def graph_2013():
    '''ฟังชั่นพล็อตกราฟท็อป10ปี2013'''
    top_10_2013 = year_2013()
    x_val = [x[0] for x in top_10_2013]
    y_val = [x[1] for x in top_10_2013]
    plt.bar(x_val, y_val, color='red')
    plt.title('Top 10 Year 2013', color='green')
    plt.show()

def graph_2014():
    '''ฟังชั่นพล็อตกราฟท็อป10ปี2014'''
    top_10_2014 = year_2014()
    x_val = [x[0] for x in top_10_2014]
    y_val = [x[1] for x in top_10_2014]
    plt.bar(x_val, y_val, color='red')
    plt.title('Top 10 Year 2014', color='green')
    plt.show()

def graph_2015():
    '''ฟังชั่นพล็อตกราฟท็อป10ปี2015'''
    top_10_2015 = year_2015()
    x_val = [x[0] for x in top_10_2015]
    y_val = [x[1] for x in top_10_2015]
    plt.bar(x_val, y_val, color='red')
    plt.title('Top 10 Year 2015', color='green')
    plt.show()

def graph_2016():
    '''ฟังชั่นพล็อตกราฟท็อป10ปี2016'''
    top_10_2016 = year_2016()
    x_val = [x[0] for x in top_10_2016]
    y_val = [x[1] for x in top_10_2016]
    plt.bar(x_val, y_val, color='red')
    plt.title('Top 10 Year 2016', color='green')
    plt.show()

allgraph()

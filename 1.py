# from bs4 import BeautifulSoup
# from lxml import html
# import xml
# import requests
#
# url = "https://movie.douban.com/chart"
# f = requests.get(url)
# soup = BeautifulSoup(f.content, "lxml")
# for k in soup.find_all('div',class_='p12'):
#    a = k.find_all('span')
#    print(a[0].string)

# import requests
#
# url = "https://movie.douban.com/chart"
# response = requests.get(url)
# content = requests.get(url).content.decode("utf-8")
# print("response headers:", response.headers)
# print("content:", content)

import pandas as pd
import xlwt                       # 不知道为啥要导入这个模块， 但导入之后就不报错， 并且成功了
df = pd.read_csv("D:/Users/acer/Desktop/大数据第二章/ch2案例资料/星巴克.csv")           # 斜杠弄反了
df.to_excel("D:/Users/acer/Desktop/大数据第二章/ch2案例资料/你好.xls")
print(df)

# from pandas import Series, DataFrame
#
# string_data = Series(['abcd', 'efgh', 'ijkl', 'mnop'])
# print(string_data)
# print("...........\n")
# string_data[0] = None                       # 可以先判断是否为空
# print(string_data)
# print("...........\n")
# print(string_data.isnull())


""""这个有用"""
# import pandas
# import xlwt
# import xlrd              # 在使用read_excel和read_csv时， 必须要导入这两个模块
#
# df_2 = pandas.read_excel("D:/Users/acer/Desktop/大数据第二章/ch2案例资料/data3.xlsx")
# print(df_2)
# df_2.to_csv("D:/Users/acer/Desktop/大数据第二章/ch2案例资料/data3.csv")
# df = pandas.read_csv("D:/Users/acer/Desktop/大数据第二章/ch2案例资料/directory.csv")
# print(df)
# df.to_excel("D:/Users/acer/Desktop/大数据第二章/ch2案例资料/data2.xls")

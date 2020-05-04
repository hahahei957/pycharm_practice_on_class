# import pandas
# import xlrd
# data = pandas.read_excel("D:/Users/acer/Desktop/大数据第3章/ch3案例资料/score.xls")
# print(data.info())
# print(data.max())
# print(data.min)
# print(data.quantile(0.5))


# x = [1,2,3,4]
# print(x)
# x.append("ni".join("131234535"))
# print(x)
#
# print(type([x*y for x in range(10) for y in range(10)]))


# def abc():
#     a = i +1
#     print(a)
#
#
# i = 2
# abc()


# 加钱
# def add(money):
#     global all
#     all += money
#
#
# def get_choice():
#     return input("请输入是否继续累计,n为退出")
# a="13"
# b = 5
#
# print("%s     %d"%(a,b))


# def a(n):
#     if n==2:
#         return 1/2
#     else:
#         if n % 2 == 1:
#             return a(n-1)-1/(n*(n-1))
#         else:
#             return a(n-1)+1/(n*(n-1))
#
# c = int(input(""))+1
# print(a(c))


# import time
#
#
# import time
#
# time.asctime((2000, 2, 26, 1, 1, 15, 15, 1, 0))
# print(time.asctime())


import calendar

# print(calendar.calendar(2019, w=2, l=1,c=6))
# print(calendar.calendar(2019, w=2, l=2,c=6))
# print(calendar.firstweekday())
#
# print(calendar.leapdays(2000, 2020))

# print(type(calendar.month(2019, 11)))
# print(type(calendar.monthrange(2019, 11)))

# year, month, day, hour, minute, second = tuple[:6]
# print(calendar.timegm((1970, 1, 1, 0, 0, 1)))

# a =range(1, 100)
# # for i in a:
# #     print(1)
# # print(a)

"""

"""

# def name(a):
#
#     def unknow(b):
#         nonlocal a
#         val = a + " will take at: " +b
#
#         return val
#     return unknow
#
# math = name("math")
# print(math("9.00"))

# flist =[]
# for i in range(3):
#     def foo(X):
#         print(x + i)
#     flist.append(foo)
# for f in flist:
#     f(2)

# import jieba
# import wordcloud
# import matplotlib.image as mpimg
# f = open("D:/Users/acer/Desktop/所有的文件/大数据课件/大数据第4章/ch4案例资料/电动车.txt", "r", encoding="utf-8")
# fill = f.read()
# f.close()
# list_fill = jieba.cut(fill)
# print(list_fill)
# temp_text = " ".join(list_fill)
# mask = mpimg.imread("D:/Users/acer/Desktop/所有的文件/大数据课件/大数据第4章/ch4案例资料/u=270540360,4103478178&fm=26&gp=0.jpg")
# # 我感觉这里是获取每个像素点的矩阵位置，通过0和1来标定位置信息
# w = wordcloud.WordCloud(width=800,
#                         height=600,
#                         background_color="white",
#                         font_path="C:/Users/acer/AppData/Local/Microsoft/Windows/Fonts/锐字锐线怒放黑简1.0.TTF",
#                         mask=mask
#                         )
# w.generate(temp_text)
# w.to_file("D:/Users/acer/Desktop/所有的文件/大数据课件/大数据第4章/ch4案例资料/aim.jpg")
# import time
#
#
# def sleeping_test(functionname):
#     def inner():
#         start = time.time()
#         print("开始1")
#         functionname()            # 调用函数f() ,就是从这里把f()封装了起来， 就是在这里调用了一下f()    【即functionname对应的对象】
#         end = time.time()
#         print("1")
#         return end-start            # 这个return这里还有问题
#     return inner
#
#
# def sl2(functionname):
#     def inner():
#
#         print("a")
#         print("开始2")
#         functionname()
#         print("2")
#         time.sleep(1)
#     return inner
#
#
# @sleeping_test
# @sl2
# def f():
#     print("_______________________1")
#     time.sleep(1)
#     print("__________________________2")
#
#
# print(f())

# value = lambda x: x**2
#
# print(list(map(value, 123)))


# from functools import reduce
#
# print(reduce(lambda x,y:x*y, [x for x in range(1,int(input(""))+1)]))

# from pymysql import *
#
# conn = connect(host='localhost',port=3306,user='root',password='267518',database='cates_jingdong',charset='utf8')
# cs1 = conn.cursor()
# count = cs1.execute('select * from goods where id<5')
# print(count)
# cs1.close()
# # 关闭Connection对象
# conn.close()
# def main():
#     find_name = input("请输入物品名称：")
#     # 创建Connection连接
#     conn = connect(host='localhost',port=3306,user='root',password='mysql',database='jing_dong',charset='utf8')
#     # 获得Cursor对象
#     cs1 = conn.cursor()
#     # # 非安全的方式
#     # # 输入 " or 1=1 or "   (双引号也要输入)
#     # sql = 'select * from goods where name="%s"' % find_name
#     # print("""sql===>%s<====""" % sql)
#     # # 执行select语句，并返回受影响的行数：查询所有数据
#     # count = cs1.execute(sql)
#     # 安全的方式
#     # 构造参数列表
#     params = [find_name]
#     # 执行select语句，并返回受影响的行数：查询所有数据
#     count = cs1.execute('select * from goods where name=%s', params)
#     # 注意：
#     # 如果要是有多个参数，需要进行参数化
#     # 那么params = [数值1, 数值2....]，此时sql语句中有多个%s即可
#     # 打印受影响的行数
#     print(count)
#     # 获取查询的结果
#     # result = cs1.fetchone()
#     result = cs1.fetchall()
#     # 打印查询的结果
#     print(result)
#     # 关闭Cursor对象
#     cs1.close()
#     # 关闭Connection对象
#     conn.cl
#     ose()
# if __name__ == '__main__':
#     main()
""""""
# class IsRightHeight(Exception):
#     def __init__(self,height):
#         self.height = height
#
#
# def test_weight():
#     weight = int(input("请输入体重："))
#     height = int(input("请输入身高"))
#     standard_weight = height-100
#     try:
#         if height<130 or height>250:
#             raise IsRightHeight(height)         # 创建一个IsRightHeight的类对象，并且对象名字也是IsRightHeight
#         if weight<(standard_weight+standard_weight*0.05) or standard_weight>(standard_weight-standard_weight*0.05):
#             print("体重正常")
#         elif weight>(standard_weight*0.05+standard_weight):
#             print("超重")
#         else:
#             print("体重不达标")
#     except IsRightHeight as result:
#
#
#
# if __name__=="__main__":
#     test_weight()

#
# """"""
#
# import sys
#
# print(sys.path)


# x=[8,7,6,5,4,3,2,1]
# print(x.pop(2))
# print(list(map(str, [1, 2, 3])))

# class Account:
#     def __init__(self,id):
#         self.id=id
#         id=1688
#
# acc=Account(100)
# print(acc.id)

#
# a = input("")
# n = len(a)
# s = ""
# for i in range(n):
#     s += (i+1)*a[i]
# print(s)

from functools import reduce
# a = "2 4 -5 10"
# a = input("")
# lis = a.split(" ")
# print(lis)
# c = list(map(lambda x: int(x) + 201, lis))
# d = list()
# for i in c:
#     if i%7!=0:
#         d.append(str(i))
# print(" ".join(d))


a = "banana"
# a = input("")
n = len(a)               # 统计个数

lis = list(map(lambda x,y:x*y, a,range(1,n+1)))
print(range(n))
print("".join(lis))



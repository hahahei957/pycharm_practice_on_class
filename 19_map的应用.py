# value = lambda x: x**2
#
# print(list(map(value, 123)))

"""
将A中的每个子元组中的第一项拿出来
匿名函数lambda返回的是冒号：右侧方程式计算的结果
"""
# A = [("a", 1), ("b", 2), ("c", 3)]
#
# print(list(map(lambda x:x[0], A)))          # 匿名函数lambda返回的是冒号：右侧方程式计算的结果


# list1 = [x for x in range(1, 9)]
# list2 = [x for x in range(1,9)]
# list3 = [x for x in range(1,9)]
#
# print(list(map(lambda x,y,z: x*y*z, list1, list2, list3)))

"""
读入一个用户输入的字符串s，构成字符串s的每个字母根据其在原始字符串s中的索引数加上1被重复指定的次数。输出新生成的字符串。
输入格式:
读入用户输入的一行字符串
输出格式:
输出新生成的字符串
输入样例:
在这里给出一组输入。例如：
banana
输出样例:
在这里给出相应的输出。例如：
baannnaaaannnnnaaaaaa
"""
# 方法1
a = input("")
n = len(a)
s = ""
for i in range(n):
    s += (i+1)*a[i]
print(s)

# 方法2
# a = "banana"
# n = len(a)               # 统计个数
# print(list(map(lambda x,y:x*y, a, i in range(n))))    # 这个是不太对的，底下的那个是对的

a = "banana"
# a = input("")
n = len(a)               # 统计个数

lis = list(map(lambda x,y:x*y, a,range(1,n+1)))·       # 指定range是从1开始的即可
print(range(n))
print("".join(lis))

"""
通过reduce实现n的阶乘的求解
"""
from functools import reduce

print(reduce(lambda x,y:x*y, [x for x in range(1,int(input(""))+1) if x > 3]),3)

print(range(10))




"""
用户输入由n个整数构成的一个字符串（相邻两个整数之间用一个空格间隔），让每个整数分别加上201得到新的数字，把不能被7整除的新数字按原来输入时的顺序输出（相邻两个整数之间用一个空格间隔）。
输入格式:
读入由n个整数构成的一个字符串（相邻两个整数之间用一个空格间隔）
输出格式:
把不能被7整除的新数字按原来输入时的顺序输出（相邻两个整数之间用一个空格间隔）
输入样例:
在这里给出一组输入。例如：
2 4 -5 10

输出样例:
在这里给出相应的输出。例如：
205 211
"""
from functools import reduce
a = "2 4 -5 10"
# a = input("")
lis = a.split(" ")
print(lis)
c = list(map(lambda x: int(x) + 201, lis))
d = [str(x) for x in c if x%7 != 0]
e = " ".join(d)                          # .join()只能连接字符类型的成员
print(e)




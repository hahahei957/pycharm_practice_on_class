"""
三边是否能构成三角形
1 2  3
"""

from math import *

# a = int(input(""))
# b = int(input(""))
# c = int(input(""))
#
#
# if a**2 + b**2 <= c** and c**2 + b**2 <= a** and a**2 + c**2 <= b**:
#     print("%d %d %d可以构成三角形"%(a, b, c))
# else:
#     print("不可以")

a = input("")
l = list()
for i in a:
    l.append(i)
l.reverse()
s = "".join(l)
if s == a:
    print("是回文数")
else:
    print("不是")

a = int(input(""))
b = int(input(""))
i = 1
j = 1
aim = 0
while True:
    print("__________________")
    if a * i > b * j:
        while True:
            if a * i == b * j:
                aim = a * i
                print("最小公约数是",a*i)
                break
            if a * i < b * j:
                break
            j += 1
            # print("11111111111111111111111")
            # print("%d和%d的最小公倍数是%d" % (a, b, a * i))
    if aim == a * i:
        break
    if a * i < b * j:
        while True:
            if a * i == b * j:
                aim = a * i
                print("最小公约数是",a*i)
                break
            if a * i > b * j:
                break
            i += 1
            # print("11111111111111111111111")
    if aim == b * j:
        break
print(aim)


a = input("")
l = list()
for i in a:
    l.append(i)
l.reverse()
s = "".join(l)
if s == a:
    print("是回文数")
else:
    print("不是")
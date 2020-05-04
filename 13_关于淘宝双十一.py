"""
数据：
[year for year in range(2009,2019)]
[0.5, 9.36, 52, 191, 352, 571, 912,1207,1682.69,2135]
测试数据:
2019--2684

我们是用的numpy去处理数据
用matplotlib.pyplot将数据展示出来
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
# 输入数据源
x = np.array([year for year in range(2009,2019)])                   # 我感觉np是将数据转换成数组/矩阵之类的
y = np.array([0.5, 9.36, 52, 191, 352, 571, 912,1207,1682.69,2135])
# 数据处理
z1 = np.polyfit(x, y, 3)           # 对x和y进行3次多项式拟合
# print(z1)                  # z1得到的是我们生成多项式的系数
p1 = np.poly1d(z1)           # p1得到的是目的3次多项式


# 将数据结果展示出来
yvals = p1(x)

plt.rcParams['font.sans-serif'] = ['SimHei']           # 这句话很重要， 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False             # 用来正常显示负号的

plot1 = plt.plot(x, y, '*', label='实际销售额')
plot2 = plt.plot(x, yvals, 'r', label='拟合销售额')
plt.xlabel("年份")                             # 不能显示中文字体
plt.ylabel("销售额(亿)")
plt.title("2009-2018淘宝销售额")

# plt.title("str",fontproperties = 'SimHei',fontsize=20)        # 需要修改字体， 不知道是不是这句话

print("拟合多项式", p1)
print("__________________________")
print("2019年预测值：", p1(2019))
print(type(x))

plt.show()                          # 显示出图像





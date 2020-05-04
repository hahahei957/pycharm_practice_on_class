"""
Matplotlib 是 Python 的绘图库，绘图界面由pyplot模块提供。
绘制箱线图的函数为 boxplot ()
使用方法:
1）导入模块  import matplotlib.pyplot as plt
2）pyplot常用函数：
savefig函数 :           plt.savefig("文件名")
title 函数 :                plt.title("str",fontproperties = 'SimHei',fontsize=20)
plt.figure
3）画图：使用Dataframe的boxplot方法

 plt.boxplot(x,labels,...)
         常用参数及说明：
         x	指定要绘制箱线图的数据；
         labels	    为箱线图添加标签
         sym	    指定异常点的形状
         vert	    是否需要将箱线图垂直摆放
         patch_artist   是否填充箱体的颜色；填充为 True
         boxprops	    设置箱体的属性，如边框色，填充色等；color箱体边框色，facecolor箱体填充色；
            例如： boxprops = {'color':'orangered','facecolor':'pink'}

"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']           # 这句话很重要， 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False             # 用来正常显示负号的
plt.figure(figsize=(10,10))
dataframe = pd.read_excel("D:/Users/acer/Desktop/所有的文件/大数据课件/大数据第3章/ch3案例资料/score.xls")

plt.title("箱型图")
# 绘制箱型图
dataframe.boxplot()
plt.savefig("D:/Users/acer/Desktop/所有的文件/大数据课件/大数据第3章/ch3案例资料/score_box.png")
# plt.show()


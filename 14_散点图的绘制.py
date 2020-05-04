"""
matplotlib库：Matplotlib 是 Python 的绘图库，主要用于二维绘图，简单的三维绘图。
pyecharts库：pyecharts 是一个用于生成 Echarts 图表的类库。
Seanborn库：Seaborn是基于matplotlib产生的一个模块，专攻于统计可视化，可以和pandas进行无缝链接
其他：ggplot库，pygal，geoplotlib......

matplotlib库基本使用方法：
import matplotlib.pyplot as plt
1.plt.plot()函数：
plt.plot(x, y, format_string, **kwargs)

    x ： X轴数据，列表或数组，可选
    y ： Y轴数据，列表或数组
    format_string ： 控制曲线的格式字符串，可选
    **kwargs ：第二组或更多(x,y,format_string)
其中要说明的是format_string，包含的主要类型有
颜色字符：'b','k'等
风格字符：'-','--'等
标记字符：每个数据点的标志方式,'.','*','o'等

"""






























import matplotlib.pyplot as plt
import pandas as pd

dataframe = pd.read_excel("D:/Users/acer/Desktop/所有的文件/大数据课件/大数据第3章/ch3案例资料/score.xls")
print(dataframe)

data_x =list(range(1,len(dataframe)+1))
data_y =dataframe['平时']
plt.scatter(data_x,data_y,s=50,c='r',marker="o",alpha=0.5)
plt.show()
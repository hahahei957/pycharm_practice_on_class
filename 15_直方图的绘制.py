import time
import matplotlib.pyplot as plt
import pandas as pd

t_01 = time.time()
t_t01 = time.process_time()

dataframe = pd.read_excel("D:/Users/acer/Desktop/所有的文件/大数据课件/大数据第3章/ch3案例资料/score.xls")

plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文不能正常显示的问题
dataframe.dropna(subset=["期末"],inplace=True)   # 剔除空值
dataframe.dropna(subset=["平时"],inplace=True)

plt.subplot(211)         # 表示我们生成了2行1列的图表，并指示当前图表为第一个

plt.hist(dataframe['期末'],bins=10,color='blue',edgecolor='k',label='期末')    # edgecolor边缘线的颜色
plt.legend()             # 声明我们使用了标签

plt.subplot(212)           # 再次声明我们的2行1列的图表，并指示当前图表为第二个

plt.hist(dataframe['平时'],bins=10,color='green',edgecolor='k',label='平时')
plt.tick_params(top='off', right='off')              # 删除上边框和有边框的单位线
plt.legend()


t_t02 = time.process_time()
t_02 = time.time()
print(t_02-t_01)
print(t_t02-t_t01)

plt.show()





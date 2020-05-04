"""
潘大是的应用
(6) pandas包中的统计函数  dataframe
df.mean()             按各列求平均值
df.median()          求中位数
df.max()               求最大值
df.min()               求最大值
df.mode()            求众数
df.quantile(q)      求q分位数
df.var()              求方差
df.std()              求标准差
DataFrame.quantile(self, q=0.5, axis=0, numeric_only=True, interpolation='linear')
df.cov()                     求协方差矩阵
df.corr()                   求相关系数（默认pearson相关系数）

几个概念的小结
方差：方差值越大说明该数据项波动越大
数值数据趋向于分散的程度
极差：最大值不最小值之差，
极差忽略了数据内部差异而仅关注数据上下界的指标
p分位数：百分之p的数据项位于或低于Xi
四分位数：
把所有数值由小到大排列幵分成四等份，处于三个分割点位置的数值就是四分位数。
四分位差：
第三四分位数不第一四分位数的差距


偏度是数据分布偏斜程度的测度
偏度系数=0为对称分布
偏度系数> 0为右偏分布
偏度系数< 0为左偏分布
偏度系数大于1或小于-1，被称为高度偏态分布；
偏度系数在0.5～1或-1～-0.5之间，被认为是中等偏态分布；


偏度系数越接近0，数据分布相对比较对称。偏斜程度就越低
偏度大于0时，比均值更小的数据更多一些，反之则是比均值更大的数据较多
偏度（skewness）
DataFrame.skew(axis=None, skipna=None, level=None, numeric_only=None, **kwargs)
用来描述数据分布的对称性，正态分布的偏度为0。计算数据样本的偏度，当偏度<0时，称为负偏，数据出现左侧长尾；当偏度>0时，称为正偏，数据出现右侧长尾；当偏度为0时，表示数据相对均匀的分布在平均值两侧，不一定是绝对的对称分布，此时要与正态分布偏度为0的情况进行区分。
当偏度绝对值过大时，长尾的一侧出现极端值的可能性较高。
峰度(Kurtosis)
DataFrame.kurt(self, axis=None, skipna=None, level=None, numeric_only=None, **kwargs)
df.kurt()峰度(Kurtosis)
用来描述数据分布陡峭或是平滑的情况。正态分布的峰度为3，峰度越大，代表分布越陡峭，尾部越厚；峰度越小，分布越平滑。很多情况下，为方便计算，将峰度值－3，因此正态分布的峰度变为0，方便比较。
在方差相同的情况下，峰度越大，存在极端值的可能性越高。
"""
import pandas as pd

dataframe = pd.read_excel("D:/Users/acer/Desktop/所有的文件/大数据课件/大数据第3章/ch3案例资料/score.xls")
print("极差：", dataframe.max()-dataframe.min())
print("标准差：", dataframe.std())
print("方差：", dataframe.var())
print("众数：", dataframe.mode())
print("中位数：", dataframe.median())

print(dataframe.describe())

print("偏度：", dataframe.skew())
print("峰度：", dataframe.kurt())
print("协方差：", dataframe.cov())
print("相关系数：", dataframe.corr())


import pandas as pd

dataframe = pd.DataFrame([1500, 760, 780, 1080, 850, 960, 2000, 1250, 1630])
print(dataframe)
print(dataframe.quantile(q=0.25))
print(dataframe.describe())



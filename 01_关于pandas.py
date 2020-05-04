# from pandas import Series
# s = Series([1, 2, 3.0, 'abc', "def"])        # 导入一个数组， 里面包含有索引（序列(Series)：一维标记数组，能够保存任何数据类型，有索引）
# print(s)
# print(s[1])             # 可以取索引对应的值


# from pandas import DataFrame                 # 数据帧（dataframe）：二维标记数据结构，可以传递行索引和列索引。
#
# data = {'state': ['a', 'b', 'c', 'd', 'e'], 'year': [2000, 2001, 2002, 2001, 2002],
#         'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
# frame = DataFrame(data, columns=['state', 'year', 'pop', 'newCol'],
#                   index=['one', 'two', 'three', 'four', 'five'])
# print(frame['state'])
# print(frame.loc['three'])


# from pandas import Series, DataFrame
# string_data = Series(['abcd', 'efgh', 'ijkl', 'mnop'])
# print(string_data)
# print("...........\n")
# string_data[0] = None                        # 将其中的一项设置为空， 再调用isnull函数，
# print(string_data.isnull())                  # isnull函数可以检查数组中每一项是否为空，并返回一个布尔值
# print(string_data.dropna())                  # dropna函数可以删除所有数据中的空值

# from pandas import Series, DataFrame
# from numpy import nan as NA                     # NA即相当于None，表明此处为空值
# data = Series([1, None, 3.5, NA, 7])            # NA即相当于None，表明此处为空值
# print(data)
# print("________________________")
# print(data.dropna())                             # 将数组中，含有空值的函数删去


# from pandas import Series, DataFrame, np
# from numpy import nan as NA
#
# data = DataFrame(np.random.randn(7, 3))
# data.iloc[:4, 1] = NA                            # 第一列的0至4个，全部被替换为空，
# data.iloc[:2, 2] = NA                            # 第二列的0至2个全部被替换为空
# print(data)
# print("...........")
# print(data.fillna(0))
# print("...........")
# print(data.fillna({1: 111, 2: 222}))          # fillna函数不改变data自身的值， 只是产生一个更改之后的返还值
# print("...........")
# print(data)

from pandas import Series, DataFrame, np
from numpy import nan as NA

data = DataFrame(np.random.randn(1000, 4))
print(data.describe())
print("\n....找出某一列中绝对值大小超过3的项...\n")
col = data[3]
print(col[np.abs(col) > 3])





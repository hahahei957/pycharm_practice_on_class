"""
用决策树(分类的一种)数实现数据的分析和预测
模拟数据
输出数据
"""

from sklearn import tree
from sklearn.model_selection import train_test_split

import pandas

dataframe = pandas.read_csv("D:/Users/acer/Desktop/所有的文件/大数据课件/大数据第3章/ch3案例资料/body.csv")
x_train = dataframe[["height", "weight"]][:10]    # 一定要用两个中括号，因为我们取得是两列，所以两列的名字一定要在该列表的同一个成员中， 而只要一个括号，只会在这个列表的两个成员中
y_train = dataframe["body"][:-2]                      # 也是后两行不能取
# print(dataframe[["body", "height"]])
clf = tree.DecisionTreeClassifier(criterion="entropy")
print(x_train)
clf.fit(x_train, y_train)                   # 判断的数据类型一定要为datafram类型的     必要时，可以通过x = dataframe(x)
x_test = dataframe[["height", "weight"]][-2:]
print(clf.predict(x_test))                             # 预测的结果

# x_test = dataframe[["height", "weight"]][-2:]



"""
无监督学习就是指算法专门接收未标注数据，并对所有的未知点做出预测 
 主要目标是发现数据中共性的东西，对观察值进行分类或者区分等

"""


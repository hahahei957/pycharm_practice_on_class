from sklearn import tree
import pandas as pd

# 读入数据集
dataframe = pd.read_csv("D:/Users/acer/Desktop/所有的文件/大数据课件/大数据第3章/ch3案例资料/body.csv")
x = dataframe[["height", "height"]]
y = dataframe["body"]

# 配置好数据处理函数f(x)的属性
clf = tree.DecisionTreeClassifier(criterion="entropy")
# 运用配置好的函数去训练得到函数h(x)
clf.fit(x[:10], y[:10])
# 预测
data_test = dataframe[["height", "weight"]][-2:]
body_test = clf.predict(x[-2:])

print(body_test)



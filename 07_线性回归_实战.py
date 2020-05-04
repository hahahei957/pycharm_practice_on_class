import pandas        # 从本地的文件导入数据时要用到pandas
from sklearn import linear_model

# 得到数据源
dataframe = pandas.read_csv("D:/Users/acer/Desktop/所有的文件/大数据课件/大数据第3章/ch3案例资料/body.csv")
x = dataframe["height"]
y = dataframe["weight"]
# 得到预测函数模型f(x)
model = linear_model.LinearRegression()               # 函数报错中含有reshape 表示这里要转换一下类型       用线性函数不知道为啥一定要转换为DataFrame的形式
x = pandas.DataFrame(x)
y = pandas.DataFrame(y)            # 对DataFrame切片也可以用列表切片的形式
# 用模型训练得到函数h(x)
model.fit(x[:10], y[:10])
print(list(model.predict(x)))
print(y)

# 得到预测结果
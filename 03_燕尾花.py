from sklearn import datasets,tree
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()
x_train,x_test,y_tarin,y_test = train_test_split(iris.data, iris.target, test_size=0.2)     # 将所有燕尾花数据按照训练数据和测试数据按8:2分开
print(x_train)
clf = tree.DecisionTreeClassifier(criterion="entropy")    # 调用决策树，产生可以处理数据的函数f(x)

clf.fit(x_train, y_tarin)                          # 用得到的某种名为clf对象来用数据训练函数h(x)
answer = clf.predict(x_test)               # 用得到的训练结果h(x)去预测待测试函数
print(answer)
print(y_test)
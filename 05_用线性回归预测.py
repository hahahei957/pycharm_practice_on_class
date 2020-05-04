from sklearn import datasets,linear_model

from sklearn.model_selection import train_test_split

diabets = datasets.load_diabetes()
x_train, x_test, y_train, y_test = train_test_split(diabets.data,diabets.target,test_size=0.2)   # 返还四个元祖的值

model = linear_model.LinearRegression()
model.fit(x_train, y_train)
print(model.predict(x_test))
print(y_test)


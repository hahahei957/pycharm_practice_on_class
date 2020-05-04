import pandas
import xlwt
dataframe = pandas.read_csv("D:/Users/acer/Desktop/大数据第二章/ch2案例资料/星巴克.csv")
# print(dataframe)
# print(dataframe.describe())
# print(dataframe.info())

# 将city下的内容为空的位置存入键值为"State/Province"的里面
dataframe["City"].fillna(dataframe["State/Province"])
# print("________________________")

# .info是将读取得到的数据进行分析，得到了数据所有的平均值、最大最小值等等
print(dataframe.info())
# print("__________")

# 这里的这个是获得一个只有一个名为city键值的字典
country_count_1 = dict()
country_count_1["city"] = dataframe["Country"].value_counts()[0:10]

print(country_count_1)
# country_count_2 = dataframe["Country"].value_counts()[0:10]
# # China_data = dataframe[dataframe["Country"] == "CN"]
# China_count_2 = dataframe["City"].value_counts()[0:10]
# print(country_count_2)
# write = pandas.ExcelWriter("D:/Users/acer/Desktop/大数据第二章/ch2案例资料/dipy.xls")
# country_count_2.to_excel(write, sheet_name="国家分布前十")
# China_count_2.to_excel(write, sheet_name="城市分布前十")
# write.save()                                                                           # 上面的操作运行到了内存里， 还需要.save存储一下

# for city in dataframe["City"]:
#     print(city)
# a = "123222222"
# print(a.split("2"))
# print(a.count("2"))
# print(a.find("2"))
#
# c = "123456"
# for i in c:
#     print(i)
# print(len(c))

# c = list()
# c.append("123")
# c += 11
# print(c)

# namelist = ["x
#
# iaowang", "xiaoming", "xiaohong", "xiaowang", "xiaowang", "xiao"]           # 这样两个挨着的是不行的， 因为i会以为自己进了一位
# for i in namelist:
#     if i == "xiaowang":
#         namelist.remove("xiaowang")
# print(namelist)


# import random
# value_list = list()
# for i in range(0, 5):
#     value_list.append(random.randint(1, 10))
# money = 5000
# for i in range(0, len(value_list)-1):              # continue在这里面可以用
#     print(value_list[i])
#     if i == len(value_list)-2:
#         print("最后一局")
#     input_value = int(input("请猜一下大小：(0代表小于，1代表大于)"))
#     if input_value and value_list[i+1] >= value_list[i]:
#         print("你赢了")
#         money = money + money/2
#     elif input_value==0 and value_list[i+1] <=value_list[i]:
#         print("你赢了")
#         money = money + money / 2
#     else:
#         print("你输了")
#         money = money - money / 2
#     i += 1


# value = input("")
# list_recv = value.split()
# a = str()
# aim_str = str()
# for temp in list_recv:
# # aim_str = "".join(sorted([x for x in temp], reverse=True))          # 将字符串变为列表,载调用列表中的排序函数，使结果倒叙
#      num = len(temp)-1
#      while num >= 0:
#          aim_str += temp[num]
#          num -= 1
#      a += " " + aim_str
#      aim_str =str()
# print(a.strip())


# from pandas import Series
# s = Series([1, 2, 3.0, 'abc', "def"])
# print(s)
# print(s[1])             # 可以取索引对应的值
# from pandas import Series, DataFrame
#
# data = {'state': ['a', 'b', 'c', 'd', 'e'], 'year': [2000, 2001, 2002, 2001, 2002],
#         'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
# frame = DataFrame(data, columns=['state', 'year', 'pop', 'newCol'],
#                   index=['one', 'two', 'three', 'four', 'five'])
# print(frame['state'])
# print(frame.loc['three'])








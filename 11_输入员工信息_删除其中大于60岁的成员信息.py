"""
测试数据：
2
a 60
b 61
输出结果：
a 60
收到的名字作为key
"""
temp = int(input(""))
info_dic = dict()
for i in range(temp):
    recv_list = input("").split()
    info_dic[recv_list[0]] = recv_list[1]
for key in info_dic:
    if int(info_dic[key]) <= 60:
        print(key,info_dic[key])
print(info_dic)


"""
将学生信息按照ID排序
测试数据：
2
002 a
001 b
输出数据：
001 b
002 a
"""
temp = int(input(""))
info_dic = dict()
for i in range(temp):
    recv_list = input("").split()
    info_dic[recv_list[0]] = recv_list[1]
key_list = list()
# 取出id键值存到一个列表中，以便对其进行排序
for key in info_dic:
    key_list.append(key)
key_list.sort()
for id in key_list:
    print(id, info_dic[id])


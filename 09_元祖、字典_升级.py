"""
删除超过60岁的员工的键值对
"""
name = input("")
age = input("")
# 数据预处理
name_tuple = tuple(name.split())
age_list = age.split()
info_dic = dict(zip(name_tuple, age_list))
# 进行数据分析
print(info_dic)
temp = len(info_dic)

keys_to_be_delete = list()
print(info_dic)
"""
将要删除的那些键值对先储存起来
再一起删掉
通过08我们实验得到，不能同时遍历和处理同一个字典
"""
for keys in info_dic:
    if int(info_dic[keys]) >= 60:
        keys_to_be_delete.append(keys)
for temp in keys_to_be_delete:
    del info_dic[temp]
print(info_dic)

# hahe xiaoming lihong wnagewei      19 28 50 45 12

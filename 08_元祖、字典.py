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
# 数据处理
# for i in range(temp):
#     try:
#         if int(info_dic[i]) > 60:
#             del info_dic[i]
#     except Exception:
#         print(Exception)
#         break
"""
字典在遍历的时候直接不允许被删除
"""
info_dic_02 = info_dic              # 我们想通过info_dict 修改info_dict_2的内容， 结果失败了， 因为两者指向同一个地址
for keys in info_dic:                   # 遍历过程中字典内部的键发生了变动，导致出错
    try:
        if int(info_dic[keys]) >= 60:
            del info_dic_02[keys]
    except Exception:
        print(Exception)

print(info_dic_02)

# temp = hahe xiaoming lihong wnagewei      19 28 50 45 12

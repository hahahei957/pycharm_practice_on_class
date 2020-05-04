"""
测试字符串：
str_txt = "hello world"

将列表中的每一项拼接成字符串
" ".join(split_list_txt)
"""


str_txt = "hello world hello hello hello hello hello hello "

if "hello" in str_txt:
    print("__________________1")
    a = str_txt.replace("hello", "nihao")        # 全都给改了
    print(a)

split_list_txt = str_txt.split(" ")
split_list_txt.remove("hello")                 # 删除第一个
print("___________________2")                  # 应该也可以通过.pop的方式
print(split_list_txt)
print(" ".join(split_list_txt))


list_txt = list(str_txt)
print("____________________3")
print(list_txt)

"""下面这种方式蛮好的"""
num = len("hello")
print(str_txt[num:])                              # 通过切片的方式





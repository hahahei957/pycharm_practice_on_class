# x = ["xiaoing", "dahong"]
# y = [1, 2]
list_1 = []
list_2 =[]
# 不需要返回值，因为我们针对的是同一个列表的修改
# 我感觉对存储东西的列表的创建，应该在总的调用即一个调用所有子方法的函数中使用


def add_member():
    name = input("请输入名字：")
    ph = int(input("请输入电话"))
    list_1.append(name)
    list_2.append(ph)
    return list_1,list_2
def delete():
    name = input("请输入要删除的：")
    if name in list_1:
        n = list_1.index(name)
        list_1.pop(n)
        list_2.pop(n)
        return list_1,list_2
    else:
        print("没有")
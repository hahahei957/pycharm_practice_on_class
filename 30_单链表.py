
# 每一个节点的内容
class Note:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkList:
    def __init__(self):
        self.head = Note()
        pass

    def add(self, first_time=False):
        data = input("请输入要添加的数据")
        a = self.head
        # 如果不是初始化阶段创建表，则我们不能从self.head开始创建链表，而是从链表尾部开始创建链表
        if not first_time:
            # 使a指向链表的末端
            while a.next is not None:
                a = a.next
        while data != "#":
            # data = input("请输入要添加的数据") 这句话要放到后面，否则我们输入的终止条件 # 也会被录入链表中

            a.next = Note(data=data)  # 每一个next都指向了下一个新的集合对象
            a = a.next
            data = input("请输入要添加的数据")

    def show_data(self):
        a = self.head.next
        while a is not None:
            print(a.data)
            a = a.next

    def delete(self):
        print("请输入要删除的数据:")
        del_target = input("")
        a = self.head
        while a.next is not None:
            if a.next.data == del_target:
                a.next = a.next.next if a.next.next is not None else None
                print("数据{}已被删除".format(del_target))
                return
            a = a.next                                                # a指向了它的下一位a.next
        print("未找到您要删除的数据")

    def update(self):
        print("请输入要修改的数据")
        data = input("")
        a = self.head
        while a.next is not None:
            if a.next.data == data:
                print("请输入修改后的数据:")
                instead_data = input("")
                a.next.data = instead_data
                return
            a = a.next                                                 # a指向了它的下一位a.next, 等于号代表左边的变量指向右边东西的地址
        print("未找到您要修改的数据")

    def insert(self):
        print("请输入要插入的位置")
        loc = int(input(""))
        print("请输入要插入的数据")
        data = input("")
        a = self.head
        for i in range(loc):
            if i == loc-1:
                # 插入的位置不是链表末尾的下一位                     # 这个地方辉耀要再看看，否则可能会蒙
                if a.next is not None:
                    # 因为我们要将a.next指向我们新插入的数据，但改完后。a.next.next将会丢失，
                    # 所以我们先将a.next.next存到temp中，再最后将temp连接到新的a.next的后面，而新的a.next前面是之前的a，此后新的a.next将会替代旧的啊。next
                    temp = a.next.next   # a.next.next可能为None
                    a.next = Note(data)
                    a.next.next = temp

                # 插入的位置是文章末尾的下一位
                else:
                    a.next.data = data
            a = a.next                                                   # a指向了它的下一位a.next, 等于号代表左边的变量指向右边东西的地址

    def isEmpty(self):
        if self.head.next is Note:
            print("链表为空")
        else:
            print("链表不为空")

    def len_LinList(self):
        a = self.head
        i = 0
        while a.next is not None:
            a = a.next
            i += 1
        print(f"链表中有{i}个数据")

    # 开饭店的老板
    def run(self):
        # 创建新链表
        self.add(first_time=True)
        # 增删改查
        while True:
            print("查询数据输入1 删除数据输入2 修改数据输入3 插入数据输入4 添加数据输入5 判断是否为空输入6统计列表长度输入7")
            select = input("")
            if select == "1":
                self.show_data()
            elif select == "2":
                self.delete()
            elif select == "3":
                self.update()
            elif select == "4":
                self.insert()
            elif select == "5":
                self.add()
            elif select == "6":
                self.isEmpty()
            elif select == "7":
                self.len_LinList()
            else:
                print("输入有误")
        pass

link_list = LinkList()
link_list.run()
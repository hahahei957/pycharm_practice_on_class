

class Note:
    def __init__(self, data=None, prior=None, next=None):
        self.data = data
        self.prior = prior
        self.next = next
        pass


class DulList:
    def __init__(self):
        self.head = Note()
        pass

    def add(self, first_time=True):
        data = input("请输入您要输入的数据")
        a = self.head
        if first_time is not True:                             # 这里不判断直接循环也是可以的
            while a.next is not None:
                a = a.next
        while data != "#":
            a.next = Note(data=data, prior=a)
            a = a.next
            data = input("请继续输入您要输入的数据")

    def show(self):
        a = self.head
        while a.next is not None:
            print(a.next.data)
            a = a.next

    def delect_data(self):
        print("请输入您要删除数据的位置")
        n = int(input(""))
        a = self.head
        i = 0
        while a.next is not None and i<=n-2:
            i += 1
            a = a.next                  # 我们让i<=n-2中减二的原因是让a指向要删除数据的前一个数据，这样好处理
        if a.next is not None:
            a.next = a.next.next
        else:
            print("您要删除的数据位置不存在，链表已经越界")

    def updata(self):
        print("请输入要修改的数据位置")
        loc = int(input(""))
        print("请输入要修改的数据内容")
        data = input("")
        a = self.head
        i = 0
        while a.next is not None:
            i += 1
            if i == loc and a.next.next is not None:    # a.next.next is not None说明还有修改值的位置并不是链表的末尾
                b = a.next.next
                a.next = Note(data=data, prior=a,  next=a.next.next)
                b.prior = a.next
                print("数据已更新")
                return
            if i == loc:                 # 此时说明修改处的位置是文章的末尾，则a.next.next是空
                a.next = Note(data=data, prior=a, next=a.next.next)   # a.next = Note(data=data, prior=a) 这样写也可以
                print("数据已更新")
            a = a.next
        print("修改数据位置越界")

    def insert(self):
        print("请输入您要插入数据的位置")
        loc = int(input(""))
        print("请输入要插入的数据")
        data = input("")
        a = self.head
        i = 0
        while a.next is not None:
            i += 1
            if i == loc:         # 这里不用向updata那里似的，这里是在a和a.next之间插入数据，不涉及a.next.next，所以不用和updata那里似的
                a.next.prior = Note(data=data, prior=a, next=a.next)
                a.next = a.next.prior
            a = a.next

    def isEmpty(self):
        if self.head.next is None:
            print("此列表为空")
        else:
            print("此列表不是空")
        return

    def run(self):
        # 初始化创建双链表
        self.add()
        self.show()
        # 增删改查
        while True:
            select = input("查询数据输入1 删除数据输入2 修改数据输入3 插入数据输入4 添加数据输入5 判断是否为空输入6")
            if select == "1":
                self.show()
            elif select == "2":
                self.delect_data()
            elif select == "3":
                self.updata()
            elif select == "4":
                self.insert()
            elif select == "5":
                self.add(first_time=False)
            elif select == "6":
                self.isEmpty()


h = DulList()
h.run()
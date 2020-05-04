
class Note:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkQuene:
    def __init__(self):
        self.front = None             # 队列头
        self.rear = None              # 队列尾
        pass

    def add(self):
        print("请输入您要输入的数据")
        data = input("")
        if self.front is None:
            self.front = Note(data=data)
            self.rear = self.front
        print("请输入您要输入的数据")
        data = input("")
        while data != "#":
            self.rear.next = Note(data=data)
            self.rear = self.rear.next
            print("请输入您要输入的数据")
            data = input("")

    def isEmpty(self):
        if self.front is None:
            print("队列为空")
            return True
        else:
            print("队列有值")
            return False

    def print_front(self):
        if self.isEmpty() is not True:
            print(self.front.data)

    def count_quene(self):
        temp = self.front
        i = 0
        while temp is not None:
            i += 1
            temp = temp.next
        print(i)
        self.num = i

    # 不知道为啥， 用while temp.data is not None:会报错
    def print_quene(self):
        temp = self.front
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def delete(self):
        if self.isEmpty() is not True:
            # 队列中只有一个元素时
            if self.front.data == self.rear.data:
                p = self.front.data
                self.front = None
                self.rear = None
                return p
            else:
                p = self.front.data
                self.front = self.front.next
                return p

    def delete_all(self):
        for i in range(self.num):
            p = self.delete()
            print(f"元素{p}删除成功")

    def run(self):
        # 初始化
        self.add()
        # print(self.front)
        # print(self.front.data)
        while True:
            print("===================================")
            print("输入1判断是否为空-输入2添加数据-输入3打印队头元素-输入4获取队列长度-输入5打印队列-输入6删除-输入7删除所有")
            i = input("")
            print("===================================")
            if i == "1":
                self.isEmpty()
            elif i == "2":
                self.add()
            elif i == "3":
                self.print_front()
            elif i == "4":
                self.count_quene()
            elif i == "5":
                self.print_quene()
            elif i == "6":
                self.delete()
            elif i == "7":
                self.delete_all()


a = LinkQuene()
a.run()
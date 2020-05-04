

class ShunXunZhan:
    def __init__(self, max_size):
        self.curlen = 0
        self.max_size = max_size
        self.stack = [None] * max_size

    def add_data(self):
        if self.curlen<=self.max_size:
            print("请输入要添加的数据")
            data = input("")
            while data != "#" and self.curlen<self.max_size:
                self.stack[self.curlen] = data
                self.curlen += 1
                data = input("")
            self.isEmpty()
            print(self.stack)

    def find(self):
        for i in self.stack:
            if i is not None:
                print(i)

    def remove_data(self):
        if self.stack[0] is not None:
            self.stack[self.curlen-1] = None
            self.curlen = self.curlen-1
            print("删除成功")
        else:
            print("栈已空，无法删除数据")

    def isEmpty(self):
        if self.curlen == 0:
            print("数据表已空")
        else:
            print("还有数据")

    def get_top_stack(self):
        print(self.stack[self.curlen-1])

    def gt(self):
        # 初始化栈
        self.add_data()
        while True:
            print("查询数据输入1 删除数据输入2 获取栈的长度输入3 获取栈顶的元素输入4 添加数据输入5 判断是否为空输入6")
            i = int(input(""))
            if i == 1:
                self.find()
            elif i == 2:
                self.remove_data()
            elif i == 3:
                print("共有%s个数据"%(self.curlen))
            elif i == 4:
                self.get_top_stack()
            elif i == 5:
                self.add_data()
            elif i == 6:
                self.isEmpty()


a = ShunXunZhan(10)
a.gt()
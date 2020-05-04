



class SqlList:
    def __init__(self, maxsize):
        self.curlen = 0
        self.maxsize = maxsize
        self.sql_list = [None]*maxsize
        pass

    def insert(self, rec=None, add=True):
        # 添加数据
        if add:
            self.sql_list[self.curlen] = rec
            self.curlen += 1
        # 插入数据
        else:
            print("当前表内的数据:", self.sql_list)
            temp = int(input("请输入要插入数据的位置"))
            if temp<0 or temp>self.curlen:
                print("只有%s个数据,插入位置超出范围"%self.curlen)
            else:
                for i in range(self.curlen-1, temp-2, -1):                     # temp对应第几个数据，也就是下标加一
                    self.sql_list[i+1] = self.sql_list[i]
                self.sql_list[temp-1] = int(input("请输入要插入的数据"))
                self.curlen += 1

    def find(self):
        for i in self.sql_list:
            print(i)
        print(self.sql_list)

    def delete(self):                                                            # 可以添加一个键表示撤销当前操作
        print("当前表内的数据:", self.sql_list)
        print("请输入要删除第几个数据")
        j = int(input(""))
        for i in range(j, self.curlen):
            self.sql_list[i-1] = self.sql_list[i]
        self.sql_list[self.curlen-1]=None
        self.curlen -= 1

    def isEmpty(self):
        if self.sql_list[1] is None:
            print("sl为空")
        else:
            for i,temp in enumerate(self.sql_list):
                if temp is None:
                    print("当前表内的数据:", self.sql_list)
                    print("SL表非空,内部还有%s个数据" % i)             # 这里也可以用self.curlen
                    break

    def add_data(self):
        print("请输入您要插入的数据，输入‘#’表示停止输入")
        while True:
            rec = input("")
            if rec != '#':
                rec = int(rec)
                self.insert(rec=rec)
            else:
                break

    def run(self):
        # 初始化顺序表（插入数据）
        # self.add_data()
        # 增删改查
        while True:                        # 可以在delete、add_data、insert中添加一个键表示撤销当前操作（如输入#表示撤销当前操作）
            print("="*50)
            print("查询数据输入1 删除数据输入2 修改数据输入3 插入数据输入4 添加数据输入5 判断是否为空输入6")
            print("=" * 50)
            users_chose = int(input(""))
            if users_chose==1:
                self.find()
            elif users_chose==2:
                self.delete()
            elif users_chose==4:
                self.insert(add=False)
            elif users_chose==5:
                self.add_data()
            elif users_chose==6:
                self.isEmpty()
            else:
                break


user = SqlList(10)
user.run()


class SqlList:
    def __init__(self, maxsize):
        self.curlen = 0
        self.maxsize = maxsize
        self.sql_list = [None]*maxsize
        pass

    def insert(self, rec=None, add=True):
        # 添加数据
        if add:
            self.sql_list[self.curlen] = rec
            self.curlen += 1
        # 插入数据
        else:
            print("当前表内的数据:", self.sql_list)
            temp = int(input("请输入要插入数据的位置"))
            if temp<0 or temp>self.curlen:
                print("只有%s个数据,插入位置超出范围"%self.curlen)
            else:
                for i in range(self.curlen-1, temp-2, -1):
                    self.sql_list[i+1] = self.sql_list[i]
                self.sql_list[temp-1] = int(input("请输入要插入的数据"))
                self.curlen += 1

    def find(self):
        for i in self.sql_list:
            print(i)
        print(self.sql_list)

    def delete(self):
        print("当前表内的数据:", self.sql_list)
        print("请输入要删除第几个数据")
        j = int(input(""))
        for i in range(j, self.curlen):
            self.sql_list[i-1] = self.sql_list[i]
        self.sql_list[self.curlen-1]=None
        self.curlen -= 1

    def isEmpty(self):
        if self.sql_list[1] is None:
            print("sl为空")
        else:
            for i,temp in enumerate(self.sql_list):
                if temp is None:
                    print("当前表内的数据:", self.sql_list)
                    print("SL表非空,内部还有%s个数据" % i)             # 这里也可以用self.curlen
                    break

    def add_data(self):
        print("请输入您要插入的数据，输入‘#’表示停止输入")
        while True:
            rec = input("")
            if rec != '#':
                rec = int(rec)
                self.insert(rec=rec)
            else:
                break

    def init_table(self):
        # 初始化顺序表（插入数据）
        # self.add_data()
        # 增删改查
        while True:
            print("="*50)
            print("查询数据输入1 删除数据输入2 修改数据输入3 插入数据输入4 添加数据输入5 判断是否为空输入6")
            print("=" * 50)
            users_chose = int(input(""))
            if users_chose==1:
                self.find()
            elif users_chose==2:
                self.delete()
            elif users_chose==4:
                self.insert(add=False)
            elif users_chose==5:
                self.add_data()
            elif users_chose==6:
                self.isEmpty()
            else:
                break


user = SqlList(10)
user.init_table()
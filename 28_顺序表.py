
class SqlList:
    def __init__(self, maxsize):
        self.culren = 0                     # 当前存放数据量,从一开始计数
        self.maxsize = maxsize              # 最多存放的数据数量
        self.sequence_table = [None] * maxsize

    def get(self):              # 获取数据
        pass

    def add_element(self, element):
        self.sequence_table[self.culren] = element     # 第i个位置也就是self.curlen对应的是self.sequencr最后一个成员对应地址的下一个地址位置
        self.culren += 1

    def updata(self, location, data):           # 修改数据
        pass

    def delete(self, locatin=None, delete_all= False):           # 删除数据
        if delete_all:
            if input("您确认要格式化顺序表吗(Y/N)")=="Y":
                self.sequence_table.clear()
                print("顺序表已被格式化")
                return
            else:
                print("已取消格式化的指令")
                return

        temp = 0
        if locatin is not None and 0<locatin<self.culren:
            # 因为range函数是左闭右开，如果直接用self.culren而不用self.curlen-1，则后面的self.sequence_table[temp+1] = None不写也可以
            for i in range(locatin-1,self.culren-1):
                self.sequence_table[i] = self.sequence_table[i+1]
                temp = i
            self.sequence_table[temp+1] = None                     # 由于最后一个位置的数据往前挪了一位，所以这里要将最后位置上的数据清除掉
            print("第{}个元素被删除成功".format(locatin))
            self.culren -= 1

    def insert(self, location, data):           # 插入数据
        if location<0 or location>self.culren:
            raise Exception("插入目标位置超出表内数据范围")
        if self.isFull():
            raise Exception("顺序表存放数据已满，继续插入数据将会溢出")
        if data is None:
            raise Exception("传入数据不能为空值")

        for i in range(self.culren, location-1, -1):            # 由于range函数是左闭右开，所以location的位置学不到，所以我们用了location-1
            self.sequence_table[i] = self.sequence_table[i-1]
        self.sequence_table[location-1] = data
        self.culren += 1

    def isFull(self):
        if self.culren == self.maxsize:
            print("顺序表已存满数据，请勿继续插入数据")
            return True
        else:
            print("顺序表已存放{}个数据".format(self.culren))
            return None

    def isEmpty(self):          # 判断表是否为空表
        if self.culren == 0:
            print("顺序表为空")
            return True
        else:
            print("顺序表已存放{}个数据".format(self.culren))
            return False

    def index_of_target(self, index_of_target):  # 检索某个元素为第几个
        for num, element in enumerate(self.sequence_table):
            if index_of_target == element:
                print("当前数据在第{}个位置上".format(num+1))
                return

        print("未检索到要查询的元素")

    def show(self):          # 展示数据
        print(self.sequence_table)

def main():
    list = SqlList(10)
    list.add_element("1")
    list.isFull()
    list.add_element("2")
    list.add_element("3")
    list.add_element("4")
    list.add_element("5")
    list.isFull()
    list.show()
    list.delete(locatin=2)
    list.show()
    list.insert(2, "2")
    list.show()
    list.index_of_target("3")
    list.index_of_target(3)                  # 里面存入的数据好像全是字符型的，所以int型的3不会被匹配到

if __name__=="__main__":
    main()

from link_queue import LinkList


class Node:
    """每个节点的元素"""

    def __init__(self, data=None, lchild=None, rchild=None, father=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild
        self.father = father


class Tree:
    # 二叉树
    def __init__(self, root=None):
        self.root = root
        self.level_list = list()  # 所有层的节点
        self.every_level = list()  # 每一层的节点
        self.user = "tree"

    # def add(self, first=False):
    #     if first:
    #         print("请一次性输入初始节点的数据")
    #         data = input("")
    #         # data的测试数据为：ABE##CF##D###
    #         self.root = Node(data=data[0])
    #
    #         # 实现树模型的建立（十分麻烦，不如用递归）
    #         loc = "left-child"
    #         self.cursor = self.root                # 创建一个指向当前节点的游标，指向文中的某一节点，并可以不断调整自己的位置
    #         for temp in data[1:]:
    #             # print(temp)
    #             if self.cursor.lchild is None and self.cursor.data != "#":               # 判断左孩子是否为空
    #                 self.cursor.lchild = Node(data=temp, father=self.cursor)
    #                 self.cursor = self.cursor.lchild
    #                 print(self.cursor.data)
    #             # TODO
    #             elif self.cursor.data == "#" and loc=="left-child" and self.cursor.father.rchild is None:    # 判断当前是否为叶子节点、并判断是否为上一节点的左孩子
    #                 self.cursor.father.rchild = Node(data=temp)
    #                 # self.cursor = self.cursor.father
    #                 loc = "right-child"
    #             # TODO
    #             elif self.cursor.data == "#" and loc=="right-child" and self.cursor.father.father.rchild is None:     # 判断当前节点是否叶子节点、并判断是否为上一节点的右孩子
    #                 self.cursor.father.father.rchild = Node(data=temp)
    #                 self.cursor = self.cursor.father.father.rchild
    #                 loc = "left-child"
    #             # 判断当前节点是否存在左孩子并且还没有右孩子，如果不是，则说明当前节点孩子满了，我们将游标移到他父亲那里
    #             elif self.cursor.lchild is not None and self.cursor.rchild is None:
    #                 self.cursor.rchild = Node(data=temp, father=self.cursor)
    #                 self.cursor = self.cursor.rchild
    #             else:
    #                 self.cursor = self.cursor.father

    # i = 0
    # def add(self, root=None, data=None):               # self.root 好像不能这么传，因为这里传的参数是一个引用，我们用root = Node(data=data[self.i])，只会让其指向新的值，这样不对
    #     self.i += 1
    #     # data的测试数据为：ABE##CF##D###
    #     # if root is None:
    #     #     self.root = Node(data=data[0])
    #     #     root = self.root
    #     # 这里类似于先序遍历
    #     print(self.i)
    #     # if self.i >= len(data):             # 防止self.i越过data的界限
    #     #     return
    #     """这里好好看看，理解一下，因为root是我们传进来的参数，是一个引用，如果在函数体里面对root进行赋值，则只会让root指向新的引用，不会传给self.root"""
    #     root = Node(data=data[self.i])                # root 从一开始的指向self.root到现在指向了Node()
    #     print(root.data)
    #     if root.data == "#":           # 递归的终止条件  但这句话应该放在root = Node(data=data[self.i])后面，因为我们要先创建出来这个节点才能去判断节点里面的值是否是#
    #         return
    #     self.add(root.lchild, data)
    #     self.add(root.rchild, data)

    i = -1

    def add(self, data):  # self.root 好像不能这么传，因为这里传的参数是一个引用，我们用root = Node(data=data[self.i])，只会让其指向新的值，这样不对
        self.i += 1
        # data的测试数据为：ABE##CF##D###
        # 这里类似于先序遍历
        # print(self.i)
        # if self.i >= len(data):             # 防止self.i越过data的界限
        #     return
        """这里好好看看，理解一下，因为root是我们传进来的参数，是一个引用，如果在函数体里面对root进行赋值，则只会让root指向新的引用，不会传给self.root"""
        root = Node(data=data[self.i])  # root 从一开始的指向self.root到现在指向了Node()
        print(root.data, end=" ")
        if root.data == "#":  # 递归的终止条件  但这句话应该放在root = Node(data=data[self.i])后面，因为我们要先创建出来这个节点才能去判断节点里面的值是否是#
            return
        root.lchild = self.add(data)  # 这里值为#的节点并没有被我们创建
        root.rchild = self.add(data)
        return root

    def add_child(self, root, target_node_data, lchild=None, rchild=None):
        if root is None:  # 递归的出口
            return
        if root.data == target_node_data:  # 得到目标节点
            if lchild is not None:
                root.lchild = Node(data=lchild)
            if rchild is not None:
                root.rchild = Node(data=rchild)
        # 遍历所有节点
        root.lchild = self.add_child(root.lchild, target_node_data, lchild, rchild)
        root.rchild = self.add_child(root.rchild, target_node_data, lchild, rchild)
        return root

    """使用递归就是将实现这个任务的中间任一次重复的过程进行程序化"""

    def pre_order(self, root):  # 先序遍历
        if root is None:
            return
        print(root.data, end=" ")
        self.pre_order(root.lchild)
        self.pre_order(root.rchild)

    def mid_order(self, root):  # 中序遍历
        if root is None:
            return
        self.mid_order(root.lchild)
        print(root.data, end=" ")
        self.mid_order(root.rchild)

    def post_order(self, root):  # 后序遍历
        if root is None:
            return
        self.post_order(root.lchild)
        self.post_order(root.rchild)
        print(root.data, end=" ")

    def level_order(self, root):  # 层序遍历
        # 这个层次遍历的特点是：每一个节点都进行将子节点存起来一起展示这个步骤 # 这个思想没有实现
        # 这里只是用来判断这个是否为一个空树
        if root.data is None:
            return
        # 我们这里就是从第一层开始，将节点自左向右一个一个的添加入队列中，再根据队列先进先出的特点
        q = LinkList()
        q.add(data=self.root, user=self.user)
        while not q.isEmpty():  # 这里没用递归，而是通过链表先进先出的特点来实现
            branch = q.delete(user=self.user)
            print(branch.data, end=" ")
            # print(1)
            if branch.lchild is not None:
                q.add(data=branch.lchild, user=self.user)
            if branch.rchild is not None:
                q.add(data=branch.rchild, user=self.user)

    def count_depth(self, root):
        if root is None:
            depth = 0
        else:
            print("11111111111")
            # print(root.data)
            ldepth = self.count_depth(root.lchild)  # 返回的是左节点的深度
            rdepth = self.count_depth(root.rchild)
            # (这个思路不错，但这里并不是这个思路)不论左右孩子谁数值大一些，只要有数值，我们的深度就可以加一，这是我们要实现的
            # 这里的思路是，
            if ldepth > rdepth:
                depth = ldepth + 1
            else:
                depth = rdepth + 1
        # print(depth)
        return depth

    # 注：我这里没有对传进来的root进行重新赋值，所以最初的root一直是指向self.root的，而我们也有权限对其的子节点进行修改
    def change_data(self, root, before_data, target_data):  # 由于这里一直传的是参数，所以直接改root.data只是改了参数的引用，不会改到树的内容
        if root is None:  # 这边虽然类似于self.add去创建一个二叉树，但不同的是这里要传进来root，因为这里的root相当于那里的data
            return
        if root.data == before_data:
            # 修改值
            root.data = target_data
            print("修改成功")
            return root  # 返回当前节点
        # 这里就相当于重新创建二叉树一样，只不过我们更改了一下root.data == before_data节点的值
        root.lchild = self.change_data(root.lchild, before_data, target_data)
        root.rchild = self.change_data(root.rchild, before_data, target_data)
        return root

    def run(self):  # data的测试数据为：ABE##CF##D###
        # 添加数据
        print("请一次性输入初始节点的数据")
        data = input("")
        self.root = self.add(data=data)
        # 先序遍历、后序遍历、层次遍历、计算树的深度、获得值为F的节点、将值为F的节点改为Z，给值为D的左孩子添加G节点
        while True:
            print("==============================")
            print("1.先序遍历、2.中序遍历、3.后序遍历、4.层次遍历、5.计算树的深度、6.获得值为F的节点、将值为F的节点改为Z，7.给值为D的左孩子添加G节点")
            print("==============================")
            chose = input("")
            if chose == "1":
                self.pre_order(self.root)
            elif chose == "2":
                self.mid_order(self.root)
            elif chose == "3":
                self.post_order(self.root)
            elif chose == "4":
                self.level_order(self.root)
            elif chose == "5":
                depth = self.count_depth(self.root)
                print("深度为%s" % depth)
            elif chose == "6":
                print("请输入要修改的节点")
                before_data = input("")
                print("请输入修改后的值")
                target_data = input("")
                self.change_data(self.root, before_data, target_data)
                print(f"先序输出结果为{self.pre_order(self.root)}")
            elif chose == "7":
                print("请输入要添加孩子的节点：")
                target_node_data = input("")
                print("请输入左孩子")
                lchild = input("")
                print("请输入右孩子")
                rchild = input("")
                self.add_child(self.root, target_node_data, lchild, rchild)
                print(f"先序输出结果为{self.pre_order(self.root)}")


if __name__ == "__main__":
    a = Tree()
    a.run()

# class Graph:
#     def __init__(self):
#
#         pass
#
#     # 顶点数、边数、顶点、边集合
#     def create_udg(self, vNum, eNum, v, e):
#         self.vNum = vNum    # 顶点数
#         self.eNum = eNum    # 边数
#         for v in vNum:
#
#
#     def run(self):
#         # 创建图
#         self.create_udg()
#         # 出度入度查询、邻接矩阵、逆邻接表
#
#
#         pass

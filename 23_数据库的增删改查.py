from pymysql import *


class JD(object):
    def __init__(self):
        # 创建Connection连接
        self.conn = connect(host='localhost', port=3306, database='cates_jingdong', user='root', password="267518", charset='utf8')
        # 获得Cursor对象
        self.cs1 = self.conn.cursor()

    def show_all_items(self):
        sql = """select * from goods"""
        self.execute_sql_to_fetch_thing(sql)

    def show_all_brands(self):
        sql = """select name from cates_brand"""
        self.execute_sql_to_fetch_thing(sql)

    def execute_sql_to_fetch_thing(self,sql):                            # 在方法中用自己类里面的方法，在前面一定要加上self
        self.cs1.execute(sql)
        fetch_value = self.cs1.fetchall()
        for fetch_thing in fetch_value:
            print(fetch_thing)


    def run(self):
        # 查看数据
        # 显示数据
        while True:
            print("----------jingdong--------------")
            print("1:查看所有商品")
            print("2:查询所有的品牌")
            print("3:查询所有的分类")
            print("4:查看所有商品")
            print("5:查看所有商品")
            print("6:查看所有商品")
            num = input("")
            if num == "1":
                self.show_all_items()
            elif num == "2":
                # 展示品牌
                self.show_all_brands()
                pass
            elif num == "3":
                # 查询单条信息
                pass


def main():
    jb = JD()
    jb.run()


if __name__ == "__main__":
    main()
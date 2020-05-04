"""
1.假设成年人的体重（整数）和身高（整数）存在此种关系：
    身高（厘米）-100 = 标准体重（千克）
如果一个人的体重与其标准体重的差值在正负5%之间，显示“体重正常”，其他则显示“
体重超标”或者“体重不达标”。编写程序根据用户输入的体重、身高判断体重正常、超标
或不达标。能处理用户输入的异常，并且使用自定义异常类来处理身高小于130cm、大于250cm的异常情况。
raise 异常类
raise 异常类对象    这两个都是引发指定异常类的实例

raise  重新引发刚刚发生的异常
"""


class IsRegihtHeight(Exception):
    def __init__(self, height):
        self.height = height


height = int(input("请输入身高："))
weight = int(input("请输入体重："))

try:
    if height < 130 or height > 250:
        raise IsRegihtHeight(height)  # 创建了一个名字为IsRegihtHeight的对象，恰好这个名字和对应的类IsRegihtHeight一样的名字
except IsRegihtHeight as result:      # 必须将这个对象换一个名字使用， 否则软件无法判断出来到底调用这个类还是调用这个对象
    print("输入的身高%d有误 ，请输入正确的身高" % result.height)
else:
    if not (weight <= (height - 100) * 0.95 or weight >= (height - 100) * (1.05)):
        print("体重正常")
    elif weight <= (height - 100 * 0.95):
        print("体重不达标")
    else:
        print("体重超标")
finally:
    print("___________________________")
    print("程序结束")

# class IsRightHeight(Exception):
#     def __init__(self,height):
#         self.height = height
#
#
# def test_weight():
#     weight = int(input("请输入体重："))
#     height = int(input("请输入身高"))
#     standard_weight = height-100
#     try:
#         if height<130 or height>250:
#             raise IsRightHeight(height)         # 创建一个IsRightHeight的类对象，并且对象名字也是IsRightHeight
#         if weight<(standard_weight+standard_weight*0.05) or standard_weight>(standard_weight-standard_weight*0.05):
#             print("体重正常")
#         elif weight>(standard_weight*0.05+standard_weight):
#             print("超重")
#         else:
#             print("体重不达标")
#     except IsRightHeight as result:
#
#
#
# if __name__=="__main__":
#     test_weight()

"""
a = 0
assert a!=0,"a的值不能为0"
"""

cournt = int(input("请输入学生的成绩"))
assert (0<=cournt<=100), "输入的成绩有误"
# assert的使用方式好奇怪，只有当里面的逻辑判断条件不成立时，
# 才会执行assert的语句
if cournt>=90:
    print("A")
elif cournt>=80:
    print("B")
elif cournt>=60:
    print("C")
else:
    print("D")
# assert 90 <= cournt <= 100, "A"
# assert 80 <= cournt < 90, "B"
# assert 70 <= cournt < 80, "C"
# assert 60 <= cournt < 70, "C"
# assert 0 <= cournt < 60, "D"


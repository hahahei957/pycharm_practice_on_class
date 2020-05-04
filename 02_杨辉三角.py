value = int(input(""))
# 第n行有n个
def do_factorial(n):
    """"计算阶乘"""
    a = 1
    for i in range(1, n+1):            # 这里一定要注意是n+1
        a *= i
        # print(a)
    return a


if value <= 2:
    print("1")
    if value == 2:
        print("1 1")
else:
    print("1")
    print("1 1")
    for row in range(3, value + 1):
        for line in range(1, row + 1):
            # 这两行负责处理每行的开头和结尾
            if line == row:
                print("1")
            elif line == 1:
                print("1", end=" ")
            # 下面负责处理杨辉三角中间夹杂着的数的数值
            else:
                # print("________________",str(row), str(line))
                a = int(do_factorial(row-1) / (do_factorial(line-1) * do_factorial(row-line)))    # 套入了一个公式
                print(str(a), end=" ")                                  # 当时除了一个错误，上面的row-line弄反了
            # else:
            #     print("1",end=" ")
            # 前面

"""
下属情况的前提是一个函数对应多个修饰器
修饰器会先去执行第一个修饰函数test1
直至执行到functionname()[functionname是对被修饰函数的调用]
此时会停止对第一个修饰器test1的执行，接着去执行第二个修饰函数test2
直至执行到functionname()[functionname是对被修饰函数的调用]，此时正式开始执行被修饰的函数
执行完被修饰的函数，程序从下往上即从test2到test1，再执行其内部fuctionname()后面的函数
整个过程就实现了对被多个修饰器修饰的函数的调用
"""
import time

def test1(functionname):
    def inner():
        start = time.time()
        print("开始1")
        functionname()            # 调用函数f() ,就是从这里把f()封装了起来， 就是在这里调用了一下f()    【即functionname对应的对象】
        end = time.time()
        print("结束1")
        return end-start
    return inner

def test2(functionname):
    def inner():

        print("a")
        print("开始2")
        functionname()
        print("结束2")
        time.sleep(1)
    return inner

@test1
@test2
def f():
    print("_______________________1")
    time.sleep(1)
    print("__________________________2")


print(f())
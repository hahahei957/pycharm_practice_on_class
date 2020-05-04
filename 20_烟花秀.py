

"""
particles 类

粒子在空中随机生成随机，变成一个圈、下坠、消失
即一个烟花是由多个粒子产生的，这个类产生的粒子构成了一个烟花

属性:
    - idx: 粒子的i代号
    - x, y: 粒子的坐标
    - vx, vy: 在坐标的变化速度
    - total: 每个烟花中含有粒子的总数
    - age: 粒子存在的时长
    - color: 颜色
    - cv: 画布
    cv = tk.Canvas(root, height=400, width=600)
    - lifespan: 最高存在时长

"""
import tkinter as tk
from PIL import Image, ImageTk
import time
import random
from math import *

GRAVITY = 0.5 # 定义重力的全局变量
colors = ['red', 'blue', 'yellow', 'white', 'green', 'orange', 'purple', 'seagreen', 'indigo', 'cornflowerblue']


class Particle:

    def __init__(self, cv, idx, total, explosion_speed, x=0, y=0, vx=0, vy=0, size=2, color="red", lifespan=2, **kwargs):
        self.id = idx
        self.x = x
        self.y = y
        self.initial_speed = explosion_speed
        self.vx = vx
        self.vy = vy
        self.total = total
        self.age = 0
        self.color = color
        # cv = tk.Canvas(root, height=400, width=600)
        self.cv = cv               # 指向了一个函数， 该函数需要每个粒子的位置作为参数
        self.cid = self.cv.create_oval(
            x - size, y - size, x+size,
            y+size, fill = self.color
        )
        self.lifespan = lifespan

    def alive(self):
        # 判断粒子的寿命是否到达了终点
        return self.age <= self.lifespan

    def expand(self):
        # 根据粒子当前状态，判断其应该继续膨胀还是自由落体
        return self.age <= 1.2

    # 其中的move
    def update(self, dt):

        self.age += dt           # 拉了这一句， 正的很。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。

        # 粒子膨胀 if  self.alive() and self.expand():
        if self.alive() and self.expand():
            move_x = cos(radians(self.id * 360 / self.total)) * self.initial_speed
            move_y = sin(radians(self.id * 360 / self.total)) * self.initial_speed
            self.cv.move(self.cid, move_x, move_y)
            self.vx = move_x / (float(dt)*1000)
            print("___________________1")

        # 自由落体状态
        elif self.alive():
            move_x = cos(radians(self.id * 360 / self.total))
            # we technically don't need to update x, y because move will do the job
            self.cv.move(self.cid, self.vx + move_x, self.vy + GRAVITY * dt)
            self.vy += GRAVITY * dt
            print("_________________2")

        # elif self.cid is not None:
        #     cv.delete(self.cid)    # 清除列表
        #     self.cid = None        # 清除
        else:
            cv.delete(self.cid)
            self.cid = None
            print("__________________3")

def simulate(cv):
    t = time.time()
    explode_points = list()
    wait_time = random.randint(10, 100)
    number_exploder = random.randint(6, 10)    # 产生烟花的数量
    for point in range(number_exploder):
        objects = list()
        x_cordi = random.randint(50, 550)
        y_cordi = random.randint(50, 150) # 烟花绽放的范围

        # 下面这几个都是关于random包中的常用函数的具体应用
        speed = random.uniform(0.5, 1.5)
        color = random.choice(colors)   # 随机选择出一个列表成员
        size = random.uniform(0.5, 3)
        explosion_speed = random.uniform(0.2, 1)
        # 每个烟花中的粒子数目
        total_particles = random.randint(10, 50)

        for i in range(1, total_particles):
            r = Particle(cv, idx=i, total=total_particles, explosion_speed=explosion_speed, x=x_cordi, y=y_cordi,
                         vx=speed, vy=speed, size=size, color=color, lifespan=random.uniform(0.6, 1.75))
            objects.append(r)
        explode_points.append(objects)
        # 即将每个粒子装入object中构成一个烟花， 再将每一个Object烟花存入explode_points之中
        # 所以explode_points这个列表储存了很多烟花下的粒子对象

    total_time = .0    # 这句我觉得大概是定义total_time为一个浮点型的0

    # 1.8s内一直扩大
    while total_time < 1.8:
        time.sleep(0.01)
        tnew = time.time()
        t, dt = tnew, tnew - t
        # TODO:上面这几句不是很懂
        # 我感觉上面这句就是
        # t = tnew
        # dt = tnew-t
        for point in explode_points:
            for item in point:
                item.update(dt)

        cv.update()               # 貌似是更新画布
        total_time += dt

    root.after(wait_time, simulate, cv)


def close(*ignore):
    """退出程序、关闭窗口"""
    global root
    root.quit()


if __name__ == '__main__':
    root = tk.Tk()
    cv = tk.Canvas(root, height=400, width=600)
    # 选一个好看的背景会让效果更惊艳！
    image = Image.open("D:/Users/acer\Desktop/zhaopian/鬼刀/Aeolian3.jpg")
    photo = ImageTk.PhotoImage(image)

    cv.create_image(0, 0, image=photo, anchor='nw')
    cv.pack()

    root.protocol("WM_DELETE_WINDOW", close)
    root.after(100, simulate, cv)
    root.mainloop()







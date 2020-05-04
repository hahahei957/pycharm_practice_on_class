""""
测试数据：
3 2 4 1
输出数据：
4 1
temp % i != 0
"""
import math


def is_prime(temp):
    i = 2
    if temp == 1:
        return False
    while True:
        if i > math.sqrt(temp) or temp == 2 or temp == 3:
            return True
        if temp % i == 0:
            return False
        i += 1


def main():
    recv_value = input("")
    recv_list = recv_value.split()
    output = str()
    for value in recv_list:
        value = int(value)
        if not is_prime(value):
            output += str(value) + " "
    print(output.strip())


if __name__ == "__main__":
    main()
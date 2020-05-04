import math
def judge_prime(value):
    m = int(math.sqrt(value))
    if value == 1:
        return False
    for i in range(2, m+2):
        if value % i == 0 and i <= m+1:        # i==m+1之前的任何一个时，才能说明这个不是素数 # 这句if说明它不是素数
            return False
    return True
def main():
    initial_value = input("").split()
    if int(initial_value[0]) >= int(initial_value[1]):
        print("Inputting illegal characters")
    else:
        for value in range(int(initial_value[0]), int(initial_value[1])-1):        # 这里的范围应该是减一， 因为否则会发生越界
            if judge_prime(value) and judge_prime(value+2) and value <= int(initial_value[1])-2:
                print(str(value), str(value+2))
if __name__ == "__main__":
    main()

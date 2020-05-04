get_val = input("")
list_val = get_val.split()
a = int(list_val[0])
b = int(list_val[1])
c = 0
sum = 0
for i in range(a, b+1):
    print("%5.d" % i, end="")
    c += 1
    if c%5 == 0:
        print("")
    sum += i
if c % 5 != 0:
    print("")
print("sum=%d" % sum)
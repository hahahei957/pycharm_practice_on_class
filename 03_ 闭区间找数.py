get_value = input("")
list_value = get_value.split()
a = int(list_value[0])
b = int(list_value[1])
c = int(list_value[2])
d = int(list_value[3])
e = 1
f = str()
for i in range(a, b+1):
    if i%c == 0 and i%d != 0:
        if e % 5 == 0:
            f += str(i) + "\n"
            e += 1
            continue
        f += str(i) + " "
        e += 1
print(f.strip())
        # if e%5==0 or i == b:
        #     f += str(i)
        #     print(f)
        #     e += 1
        #     continue
        # e += 1
        # f += str(i)
        # print(int(i), end=" ")
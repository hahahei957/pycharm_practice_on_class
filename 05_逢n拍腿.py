a = int(input(""))
c=0
for i in range(a, 101):
    if i%a==0 or i%10==a:
        c += 1
print(c)
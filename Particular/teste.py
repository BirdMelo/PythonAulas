num = int(input("num: "))
for i in range(num, 0, -1):
    num *= i
    print(i)
print(num)

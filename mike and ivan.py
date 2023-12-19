min = 1000
a = int(input()) # деньги Майкла
b = int(input()) # деньги Ивана
if (a >= min) and (b >= min):
    print(2)
elif (a >= min) and (b < min):
    print("Mike")
elif (a < min) and (b >= min):
    print("Ivan")
elif (a < min) and (b < min) and ((a + b) >= min):
    print(1)
else:
    print(0)
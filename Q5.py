n = int(input("enter value of n:"))
f1 = 0
f2 = 1

for i in range(0,n+1):
    if(n<=1):
        print(1)
    else:
        fabonacci = f1+f2,
        f1 = f2,
        f2 = fabonacci
        print(fabonacci)
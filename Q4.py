n = int(input("enter value of n:"))

for i in range (2,n):
    if(n%i==0):
        print(n,"is not prime number")
    else:
        print(n,"is even number")
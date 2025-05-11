#print the first n even numbers using a loop
n = int(input("enter vaule of n:"))

for i in range (1,n+1):
    if(i%2==0):
        print(i)
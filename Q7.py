#count how many digits a no. has without converting to string
num = int(input("Enter a number: "))
count = 0  
while num > 0:
    count += 1  
    num //= 10  

print(count)


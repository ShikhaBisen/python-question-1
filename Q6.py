# write a program to find the sum of digits of a numbers 
num = int(input("Enter a number: "))  
sum_digits = 0 

while num > 0:
    sum_digits += num % 10
    num //= 10 

print(f"Sum of digits: {sum_digits}")

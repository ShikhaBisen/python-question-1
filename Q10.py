# print the sum of all numbers divisible by 3 or 5 below 100 
total_sum = 0
for num in range(1, 100):
    if num % 3 == 0 or num % 5 == 0:
        print(num)  
        total_sum += num  
print(total_sum )

#create a calculator that supports +,-, *,/ using conditional 
a = int(input("enter the value of a:"))
b = int(input("enter the value of b:"))
operator = input("enter operator +,-,*,/:")

if(operator == "+"):
    print("a+b=",a+b)
elif(operator == "-"):
    print("a-b=",a-b)
elif(operator == "*"):
    print("a*b=",a*b)
elif(operator == "/"):
    print("a/b=",a/b)   
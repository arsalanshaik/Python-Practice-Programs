def add (num1, num2):
    return num1+num2


def sub(num1, num2):
    return num1-num2


def mul(num1, num2):
    return num1*num2


def div(num1, num2):
    return num1/num2


def mod(num1, num2):
    return num1%num2


num1 = float(input("Enter Number 1:"))

num2 = float(input("Enter Number 2:"))

print("""1.Addition
2.Subtraction
3.Multiplication
4.Divison
5.Modulus
""")


operation = int(input("Enter the Operation to Perform:"))

if operation == 1:
    print(add(num1,num2))

elif operation == 2:
    print(sub(num1,num2))

elif operation == 3:
    print(mul(num1,num2))

elif operation == 4:
    print(div(num1,num2))

elif operation == 5:
    print(mod(num1,num2))

else:
    print("Enter Available Option for Operation")
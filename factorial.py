def factorial(num):
    factorial = 1
    if num < 0:
        print("Factorial Doesn't Exist for negative numbers")
    elif num == 0:
        print("Factorial of 0 is 1")
    else:
        for i in range(1, num + 1):

            factorial = factorial * i
    print("Factorial of {num} is {factorial}".format(num=num, factorial=factorial))


factorial(5)
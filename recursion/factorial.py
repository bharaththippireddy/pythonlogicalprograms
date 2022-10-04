def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)


n = int(input("Enter a number"))
print("Factorial of ", n, " is", factorial(n))


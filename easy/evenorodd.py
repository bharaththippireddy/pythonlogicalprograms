num = int(input("Enter a number"))
if num <= 0:
    print(num, ' is invalid')
else:
    if num % 2 == 0:
        print(num, " is even")
    else:
        print(num, "is odd")


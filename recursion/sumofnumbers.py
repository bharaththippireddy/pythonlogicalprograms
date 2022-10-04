def sum_of_numbers(num):
    if num <= 1:
        return num
    else:
        return num + sum_of_numbers(num-1)


n = int(input("Enter a number"))
print("Sum of numbers is ", sum_of_numbers(n))


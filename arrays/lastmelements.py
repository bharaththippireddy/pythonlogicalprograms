numbers = [1, 3, 2, 5, 4]
m = int(input("Enter a number"))
for i in range(len(numbers)-m, len(numbers)):
    print(numbers[i], end=" ")


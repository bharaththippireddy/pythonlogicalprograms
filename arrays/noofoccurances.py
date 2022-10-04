numbers = [10, 20, 30, 10, 20, 40, 100]
count = 0
number = int(input("Enter a number"))
for i in range(len(numbers)):
    if numbers[i] == number:
        count += 1

print(count)
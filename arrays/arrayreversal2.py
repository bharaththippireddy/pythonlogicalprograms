numbers = [10, 20, 30, 4, 5, 3]
reversed_numbers = []
for i in range(len(numbers)-1, -1, -1):
    reversed_numbers.append(numbers[i])

print(reversed_numbers)
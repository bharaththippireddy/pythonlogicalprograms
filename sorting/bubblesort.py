numbers = [20, 10, 100, 3, 8, 199]
i = 0
swapped = True
while swapped:
    swapped = False
    for j in range(len(numbers)-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            swapped = True


print(numbers)

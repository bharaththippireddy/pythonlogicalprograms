numbers = [1, 3, 2, 5, 4]
for i in range(1, len(numbers)-1):
    if numbers[i-1] < numbers[i] > numbers[i+1]:
        print(numbers[i])
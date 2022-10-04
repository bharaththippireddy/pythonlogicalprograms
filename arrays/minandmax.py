numbers = [10, 20, 30, 4, 5, 3]
max_result = numbers[0]
min_result = numbers[0]

for i in range(1, len(numbers)):
    if numbers[i] > max_result:
        max_result = numbers[i]
    elif numbers[i] < min_result:
        min_result = numbers[i]

print(max_result)
print(min_result)
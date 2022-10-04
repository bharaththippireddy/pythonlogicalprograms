numbers = [10, 20, 30, 10, 20, 40, 100]
number = int(input("Enter a number"))
numbers2 = []
for i in range(len(numbers)):
    if numbers[i] == number:
        numbers2 = numbers[0:i] + numbers[i+1:len(numbers)]
        break
print(numbers2)

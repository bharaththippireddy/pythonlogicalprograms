def linear_search(lst, key):
    for i in range(0, len(lst)):
        if lst[i] == key:
            return i
    return -1


numbers = [20, 30, 1, 2, 3, 8]
key = int(input('Enter a number to search'))
result = linear_search(numbers, key)
if result == -1:
    print('Key not found')
else:
    print('Key found at ',result)
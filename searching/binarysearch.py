def binary_search(lst , key):
    low = 0
    mid = 0
    high = len(lst)-1

    while low <= high:
        mid = (low+high) // 2
        if lst[mid] < key:
            low = mid + 1
        elif lst[mid] > key:
            high = mid - 1
        else:
            return mid
    return -1

numbers = [20, 30, 40, 80, 100]
key = int(input('Enter a number to search'))
result = binary_search(numbers, key)
if result == -1:
    print('Key not found')
else:
    print('Key found at ',result)
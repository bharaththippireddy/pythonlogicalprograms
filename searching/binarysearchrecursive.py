def binary_search_recursive(lst , key, low, high):
    if high >= low:
        mid = (high+low) // 2
        if lst[mid] == key:
            return mid
        elif lst[mid] > key:
            return binary_search_recursive(lst, key, low, mid-1)
        else:
            return binary_search_recursive(lst, key, mid+1, high)
    else:
        return -1


numbers = [20, 30, 40, 80, 100]
key = int(input('Enter a number to search'))
result = binary_search_recursive(numbers, key, 0, len(numbers)-1)
if result == -1:
    print('Key not found')
else:
    print('Key found at ',result)
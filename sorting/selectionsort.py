def selection_sort(array):
    length = len(array)
    for i in range(length-1):
        min_index = i
        for j in range(i+1,length):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


array = [100, 4, 30, 6 ,99]
print(selection_sort(array))
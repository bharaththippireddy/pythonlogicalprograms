m1 = [[1, 2, 3],
      [4, 5, 6],
      [9, 8, 7]]

swap_column_1 = int(input('Enter column1'))
swap_column_2 = int(input('Enter column2'))

for i in range(len(m1)):
    temp = m1[i][swap_column_1-1]
    m1[i][swap_column_1 - 1] = m1[i][swap_column_2-1]
    m1[i][swap_column_2 - 1] = temp


for i in m1:
    print(i)
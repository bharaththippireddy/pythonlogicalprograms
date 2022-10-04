m1 = [[1, 2, 3],
      [4, 5, 6],
      [9, 8, 7]]

swap_row_1 = int(input('Enter row1'))
swap_row_2 = int(input('Enter row2'))

for i in range(len(m1)):
    temp = m1[swap_row_1-1][i]
    m1[swap_row_1 - 1][i] = m1[swap_row_2 - 1][i]
    m1[swap_row_2 - 1][i] = temp

for i in m1:
    print(i)
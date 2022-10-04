m1 = [[1, 2, 3],
      [4, 5, 6],
      [9, 8, 7]]

result = [[0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]]

for i in range(len(m1[0])):
    for j in range(len(m1)):
        result[i][j] = m1[j][i]

for i in result:
    print(i)
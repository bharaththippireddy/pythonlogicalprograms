m1 = [[1, 2, 3],
      [4, 5, 6],
      [9, 8, 7]]
m2 = [[1, 2, 3],
      [4, 5, 6],
      [9, 8, 7]]
result = [[0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]]

for i in range(len(m1)):
    for j in range(len(m1[0])):
        result[i][j] = m1[i][j]+m2[i][j]

for i in result:
    print(i)
m1 = [[1, 2],
      [2, 4]]

result = [[0, 0],
      [0, 0]]

for i in range(len(m1[0])):
    for j in range(len(m1)):
        result[i][j] = m1[j][i]

symmetric = True
for i in range(len(m1[0])):
    for j in range(len(m1)):
        if result[i][j] != m1[i][j]:
            symmetric = False
            break

print(symmetric)

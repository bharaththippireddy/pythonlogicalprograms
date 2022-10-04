m1 = [[1, 2, 3],
      [4, 5, 6],
      [9, 8, 7]]

for i in range(len(m1)):
    for j in range(len(m1[0])):
        if (i+j) == (len(m1[0])-1):
            print(m1[i][j])
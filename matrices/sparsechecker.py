m1 = [[1, 0, 3],
      [4, 5, 0],
      [0, 0, 0]]
count = 0
for i in range(len(m1)):
    for j in range(len(m1[0])):
        if m1[i][j] == 0:
            count += 1

if count > (len(m1)*len(m1[0]))/2:
    print('Sparse Matrix')
else:
    print('Not a Sparse Matrix')
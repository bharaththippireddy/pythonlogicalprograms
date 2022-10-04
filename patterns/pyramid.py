num = int(input('Enter a number'))
aN = 97
k = (2 * num) - 2
for i in range(0 ,num):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i+1):
        character = chr(aN)
        print(character,end=" ")
        aN += 1
    print()

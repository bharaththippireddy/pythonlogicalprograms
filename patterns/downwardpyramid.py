num = int(input('Enter a number'))
aN = 97
k = (2 * num) - 2
for i in range(num , 0, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i):
        character = chr(aN)
        print(character,end=" ")
        aN += 1
    print()

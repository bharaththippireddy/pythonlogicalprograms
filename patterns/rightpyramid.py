num = int(input('Enter a number'))
for i in range(0, num):
    for j in range(0 , i + 1):
        print("*",end=" ")
    print("\r")
for i in range(num-1, 0,-1):
    for j in range(0, i):
        print("*",end=" ")
    print("\r")

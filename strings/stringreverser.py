s = input("Enter a string")
for i in range(len(s)-1, -1, -1):
    print(s[i], end="")
print(input()[::-1])
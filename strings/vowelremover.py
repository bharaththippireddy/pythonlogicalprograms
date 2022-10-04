import re
print(re.sub("[aeiou]", "", input("Enter a string")))

s = input('Enter a string')
l = []
for i in s:
    if i not in ('a', 'e', 'i', 'o', 'u'):
        l.append(i)
print("".join(l))
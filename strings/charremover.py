s = input('Enter a string')
c = input('Enter a character to remove')
output = ""
i = 0
length = len(s)
while i<length:
    if s[i] == c:
        output = s[0:i] + s[i+1:length]
        break
    i = i + 1
print("Charater index is ",i)
print("Output Is: ",output)
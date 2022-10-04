num = int(input('Enter a number'))
result = 0
temp = num
while num != 0:
    digit = num % 10
    result = result + digit
    num = num // 10
print("Niven" if temp % result == 0 else "Not Niven")

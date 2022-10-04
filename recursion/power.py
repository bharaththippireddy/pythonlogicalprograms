def power(base, exp):
    if exp == 1:
        return base
    else:
        return base * power(base, exp-1)


b = int(input("Enter the base"))
e = int(input("Enter the exponent"))

print(power(b, e))
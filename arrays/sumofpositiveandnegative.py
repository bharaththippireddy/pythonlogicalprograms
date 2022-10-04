numbers = [-10, 20, -30, 4, 5, -3]
p_result = 0
n_result = 0
for i in numbers:
    if i > 0:
        p_result += i
    elif i < 0:
        n_result += i

print(p_result)
print(n_result)


s = input('Enter a string')
for word in s.split():
    if len(word) % 2 == 0:
        print(word, end=' ')
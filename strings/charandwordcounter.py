s = input('Enter a string')
char_count = 0
word_count = 0
for c in s:
    char_count = char_count + 1
    if c == " " or c == "\t" or c == "\n":
        word_count = word_count + 1
print("Char Count ",char_count)
print("Word Count",word_count+1)
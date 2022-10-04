class Stack:
    def __init__(self, size):
        self.stack = []
        self.capacity = size
        self.top = -1

    def push(self, data):
        if not self.is_full():
            self.stack.append(data)
            self.top += 1

    def pop(self):
        if self.is_empty():
            return "No elements in the stack"
        else:
            self.top-=1
            return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "No elements in the stack"
        else:
            return self.stack[self.top]

    def size(self):
        return self.top + 1

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        return self.size() == self.capacity

def string_reverser(s):
    stack = Stack(len(s))
    i = 0
    while i < len(s):
        stack.push(s[i])
        i = i + 1
    reversed = ''
    while not stack.is_empty():
        reversed += stack.pop()
    print(reversed)

def check(s):
    stack = Stack(len(s))
    for i in range(0, len(s)):
        x = s[i]
        if x == '(' or x == '[' or x == '{':
            stack.push(x)
            continue
        if stack.is_empty():
            return False
        y = stack.pop()
        if x == ')':
            if y == '{' or y == '[':
                return False
        elif x == ']':
            if y == '{' or y == '(':
                return False
        elif x == '}':
            if y == '[' or y == '(':
                return False
    return stack.is_empty()

print(check('({[]}'))















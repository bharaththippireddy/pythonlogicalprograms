class Stack:
   def __init__(self, size):
      self.stack = []
      self.capacity = size
      self.top = -1

   def push(self, data):
      if not self.isFull():
         self.stack.append(data)
         self.top += 1

   def peek(self):
       if self.isEmpty():
           return ("No elements in the Stack")
       else:
        return self.stack[self.top]

   def pop(self):
       if self.isEmpty():
           return ("No elements in the Stack")
       else:
           self.top-=1
           return self.stack.pop()

   def size(self):
       return self.top + 1

   def isEmpty(self):
       return self.size() == 0

   def isFull(self):
       return self.size() == self.capacity


stack = Stack(4)
stack.push("Mon")
stack.push("Tue")
print(stack.pop())
print(stack.peek())
stack.push("Wed")
stack.push("Thu")
print(stack.pop())
print(stack.pop())
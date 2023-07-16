class Stack:
    def __init__(self,size):
        self.stack = []
        self.size = size

    def push(self,data):
        if len(self.stack) >= self.size:
            print('stacl is over flow')
        else:
            self.stack.append(data)
    
    def pop(self):
        if len(self.stack) <= 0:
            print('stack is empty')
        else:
            self.stack.pop()

    def top(self):
        if len(self.stack) <= 0:
            print('stack is empty')
        else:
            print(self.stack[-1])

    def isEmpty(self):
        if len(self.stack) <= 0:
            print('empty')
        else:
            print('not empty')

    def size_stack(self):
        print(len(self.stack))

    def __str__(self):
        return " ".join([str(i) for i in self.stack])
    
S = Stack(6)
S.pop()
S.isEmpty()
for i in range(10):
    S.push(i)
print(S)
S.pop()
S.pop()
print(S)
S.top()
S.isEmpty()
S.size_stack()
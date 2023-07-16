class Array:
    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.arr = [0] * self.capacity

    def push(self,n):
        if self.length == self.capacity:
            self.resize()

        self.arr[self.length] = n 
        self.length += 1

    def resize(self):
        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity

        for i in range(self.length):
            newArr[i] = self.arr[i]
        
        self.arr = newArr

    def pop(self):
        if self.length>0:
            self.length -= 1

    def get(self,i):
        if i < self.length:
            return self.arr[i]


    def insert_at(self,i,n):
        if i < self.length:
            self.arr[i] = n

    def print(self):
        for i in range(self.length):
            print(self.arr[i])

A = Array()
A.push(1)
A.push(2)
A.push(3)
A.push(4)
A.push(5)
A.pop()
print(A.get(3))
A.print()
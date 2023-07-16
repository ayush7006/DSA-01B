class Array():
    def __init__(self):
        self.arr = []

    def insert(self,data):
        for i in data:
           self.arr.append(i)

    def insert_at(self,data,pos):
        if pos < len(self.arr):
            for i in data:
                self.arr.insert(pos, i)
                pos += 1
        else:
            print("index is not find")

    def read(self,data):
        if data in self.arr:
            print("index of", data, "is", self.arr.index(data))
        else:
            print("not in array")    

    def delete(self,pos):
        self.arr.pop(pos)

    def update(self,data,pos):
        if pos < len(self.arr):
            self.arr[pos -1 ] = data
        else:
            print("index is not define")
        

    def print(self):
        for i in self.arr:
            print(i)


l = Array()
l.insert([2,3,4])
l.insert_at([2,3,4], 1)
l.delete(5)
l.update(5, 1)

l.print()
l.read(4)
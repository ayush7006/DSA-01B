"""class Array(object):
    def __init__(self,ary_size,ary_type):
        self.ary_size = len(list(map(ary_type, range(ary_size))))
        self.ary_items = [ary_type(0)] * ary_size  # initalize array with zero

    def __str__(self):
        return " ".join([str(i) for i in self.ary_items])



    def search(self,keytosearch):
        for i in range(self.ary_size):
            if self.ary_items[i] == keytosearch :
                return print("position",i)
                
        return print("not found")


    def insert(self,item,position):
        if self.ary_size > position :
            for i in range(self.ary_size - 2, position -1, -1):
                self.ary_items[i+1] = self.ary_items[i]
            self.ary_items[position] = item
        else:
            print('array size list ', self.ary_size)


    def delete(self,itme,position):
        if self.ary_size > position :
            for i in range(position,self.ary_size -1 ):
                 self.ary_items[i] = self.ary_items[i + 1]
        else:
            print('array size list ', self.ary_size)    


a=Array(10,int)
a.insert(0, 1)
a.insert(1, 2)
a.insert(2, 3)
a.insert(3, 4)
a.insert(4, 5)
a.insert(5, 6)
a.insert(6, 7)
a.delete(4, 5)
a.search(4)
#print(a)"""

class Array:
    def __init__(self,size):
        self.size = size
        self.arr = [0] * self.size
        self.len = 0

    def push(self,n):
        if self.len < self.size:
            self.arr[self.len] = n
            self.len += 1
        else:
            print('array is full')

    def pop(self):
        if self.len > 0:
            self.len -= 1
        else:
            print('index not found')

    def get(self,i):
        if i < self.len:
            print(self.arr[i])

    def insert_at(self,i,n):
        if i < self.len:
            self.arr[i] = n
        else:
            print('index not found')

    def print(self):
        for i in range(self.len):
            print(self.arr[i])

A = Array(6)
A.push(1)
A.push(2)
A.push(3)
A.push(4)
A.pop()
A.get(2)
A.insert_at(2, 4)
A.print()
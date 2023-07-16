class Pair:
    def __init__(self,key,val):
        self.val = val
        self.key = key
    
class HashMap:
    def __init__(self):
        self.size = 0
        self.cap = 2
        self.map = [None,None]

    def hash(self,key):
        index = 0
        for chr in key:
            index += ord(chr)
        return index % self.cap
    
    def get(self,key):
        index = self.hash(key)
        while self.map[index].key != None:
            if self.map[index].key == key:
                return self.map[index].val
            index += 1
            index = index % self.cap
        return None    
    def put(self,key,val):
        index = self.hash(key)
        while True:
            if self.map[index] == None:
                self.map[index] = Pair(key,val)
                self.size += 1
                if self.size >= self.cap // 2:
                    self.rehash()
                return 

            if self.map[index].key == key:
                self.map[index].val = val
                return
            index +=1
            index = index % self.cap

    def rehash(self):
        self.cap = self.cap * 2
        newMap = [None]*self.cap

        oldMap = self.map
        self.map = newMap
        self.size = 0
        for pair in oldMap:
            if pair:
                self.put(pair.key,pair.val)

    def remove(self,key):
        if not self.get(key):
            return 
        index = self.hash(key)
        while True:
            if self.map[index].key==key:
                self.map[index] = None
                self.size -= 1
                return
            index +=  1
            index = index % self.cap

    def print(self):
        for pair in self.map:
            if pair:
                print(pair.key,pair.val)    

H = HashMap()
H.put('ayush','007')
H.put('ajay','004')
H.print()
print(H.get('ayush'))
H.remove('ajay')
H.put('shashank','004')
H.print()
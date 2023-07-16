class LNode:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None
    

class doubly_ll:
    def __init__(self):
        self.head = LNode(0)
        self.tail = LNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, index):
        cur = self.head.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        
        if cur and cur != self.tail and index == 0:
            return cur.val
        return -1
    
    def addAtHead(self,val):
        node, prev, next = LNode(val), self.head, self.head.next
        node.next, node.prev = next, prev
        next.prev = node
        prev.next = node
        
    def addAtEnd(self,val):
        node, prev, next = LNode(val), self.tail.prev, self.tail
        node.next, node.prev = next, prev
        next.prev = node
        prev.next = node

    def addAtIndex(self,index,val):
        next = self.head.next
        while next and index>0:
            next = next.next
            index -= 1
        if next and index == 0:
            node, prev = LNode(val), next.prev
            node.next, node.prev = next, prev
            next.prev = node
            prev.next = node

    def deleteAtIndex(self, index):
        node = self.head.next
        while node and index > 0:
            node = node.next
            index -= 1
        
        if node and node != self.tail and index == 0:
            node.prev.next = node.next
            node.next.prev = node.prev


dl = doubly_ll()

dl.addAtEnd(9)
dl.addAtEnd(8)
dl.addAtEnd(7)
dl.addAtHead(10)
dl.addAtHead(11)
dl.addAtHead(12)
dl.addAtIndex(3,3)
dl.deleteAtIndex(3)
print(dl.get(3))
class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkList:
    def __init__(self):
        self.head = None
    
    def ins_beg(self,data):
        self.head = Node(data,self.head)
    
    def PPrint(self):
        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next
    
    def ins_mid(self,index,data):
        if index < 0 or index > self.get_len():
            return print('err')
        if index == 0:
            self.ins_beg(data)
        itr = self.head
        count = 0
        while itr:
            if count == index -1:
                itr.next = Node(data,itr.next)
                break
            itr = itr.next
            count+=1
        
    def ins_end(self,data):
        itr = self.head
        while itr:
            if not itr.next:
                itr.next = Node(data)
                break
            itr = itr.next

    def get_len(self):
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count+=1
        return count
    
    def dele(self,index):
        itr = self.head
        count = 1
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count +=1

# ll = LinkList()
# ll.ins_beg(4)
# ll.ins_beg(3)
# ll.ins_beg(2)
# ll.ins_end(6)
# ll.ins_mid(2,7)
# ll.ins_end(10)
# ll.dele(4)
# ll.PPrint()

class DLL:
    def __init__(self):
        self.head ,self.tail = None,None
    def ins_head(self,data):
        if not self.head:
            self.head  = Node(data,self.head)
            self.tail = self.head
        else:
            node = Node(data,self.head)
            self.head.prev = node
            self.head = node
    def ins_tail(self,data):
        if not self.tail:
            self.tail  = Node(data,None,self.tail)
            self.head = self.tail
        else:
            node = Node(data,None,self.tail)
            self.tail.next = node
            self.tail = node

    def PPrint(self):
        itr = self.tail
        while itr:
            print(itr.data)
            itr = itr.prev

    def dele(self,index):
        itr = self.head
        while itr and index > 0:
            itr = itr.next
            index -=1
        
        if itr and itr != self.tail and index == 0:
            itr.prev.next = itr.next
            itr.next.prev = itr.prev

dl = DLL()

# dl.ins_tail(7)
# dl.ins_tail(8)
# dl.ins_tail(9)
# dl.ins_head(6)
# dl.ins_head(5)
# dl.ins_head(4)
# dl.dele(3)
# dl.PPrint()



class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkList:
    
    def __init__(self):
        self.head = None
    
    def ins_beg(self,data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next

    def get_len(self):
        itr = self.head
        len = 0
        while itr:
            itr = itr.next
            len += 1
        return len
 
    def ins_at_end(self,data):
        if self.head is None:
            self.head = Node(data)
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)
    
    def ins_at_mid(self,index,data):
        if index <0 or index> self.get_len():
            raise Exception("Invslid Index")
        if index == 0:
            self.ins_beg(data)
            return
        itr = self.head
        count = 0
        while itr:
            if count == index -1:
                itr.next = Node(data,itr.next)
                break
            itr = itr.next
            count += 1
    
    def dele(self,index):
        if index < 0 or index > self.get_len():
            raise Exception("Invslid Index")
        if index == 0:
            self.head = self.head.next
        itr = self.head
        count = 0
        while itr:
            if count == index:
               itr = itr.next
               break
            itr = itr.next
            count += 1




ll = LinkList()
ll.ins_beg(1)
ll.ins_at_end(4)
ll.ins_at_end(5)
ll.ins_at_end(6)
ll.ins_beg(7)
ll.ins_at_end(5)
ll.ins_at_mid(4,11)
ll.dele(0)
ll.dele(0)
ll.dele(0)
ll.print()
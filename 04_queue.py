class Queue():
    def __init__(self,size):
        self.queue = []
        self.size = size

    def enque(self,data):
        if len(self.queue) >= self.size :
            print('queue is overflow')
        else:
            self.queue.append(data)

    def deque(self):
        if len(self.queue) <= 0 :
            print('queue is empty ')
        else:
            self.queue.pop(0)
    
    def front(self):
        if len(self.queue) <= 0 and len(self.queue) >= self.size :
            print('queue is empty or full ')
        else:
            print(self.queue[0])
    
    def rear(self):
        if len(self.queue) <= 0 and len(self.queue) >= self.size :
            print('queue is empty or full ')
        else:
            print(self.queue[-1])

    def isEmpty(self):
        print(len(self.queue) <= 0)
                
    def isFull(self):
        print(len(self.queue) >= self.size)

    def __str__(self):
        return " ".join([str(i) for i in  self.queue])

Q = Queue(10)
Q.isEmpty()
for i in range(10):
    Q.enque(i)
Q.isFull()
print(Q)
Q.deque()
Q.deque()
Q.deque()
print(Q)
Q.front()
Q.rear()
Q.isEmpty()
Q.isFull()
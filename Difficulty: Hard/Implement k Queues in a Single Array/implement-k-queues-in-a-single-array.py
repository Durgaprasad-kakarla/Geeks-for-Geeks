from collections import deque
class kQueues:

    def __init__(self, n, k):
        # Initialize your data members
        self.arr=[deque() for _ in range(k)]
        self.k=k
        self.n=n
        self.tot=0
        

    def enqueue(self, x, i):
        # Enqueue element x into queue number i
        queue=self.arr[i]
        queue.append(x)
        self.tot+=1
        self.arr[i]=queue
        

    def dequeue(self, i):
        # Dequeue element from queue number i
        queue=self.arr[i]
        if queue:
            ele=queue.popleft()
            self.tot-=1
            return ele
        return -1

    def isEmpty(self, i):
        # Check if queue i is empty
        queue=self.arr[i]
        if queue:
            return False
        return True
        
        
    def isFull(self):
        # Check if array is full
        # print(self.arr)
        # print(self.n,self.k,self.tot)
        if self.tot>=self.n:
            return True
        return False
        
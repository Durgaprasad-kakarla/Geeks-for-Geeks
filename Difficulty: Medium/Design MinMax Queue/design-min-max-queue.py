import heapq

class SpecialQueue:
    def __init__(self):
        # Define Data Structures
        self.queue = [] 
        self.min_heap = [] 
        self.max_heap = []
        heapq.heapify(self.min_heap)
        heapq.heapify(self.max_heap)
    
    def enqueue(self, x):
        # Insert element into the queue
        heapq.heappush(self.min_heap,x)
        heapq.heappush(self.max_heap,-x)
        self.queue.append(x)

    def dequeue(self):
        # Remove element from the queue
        x=self.queue.pop(0)
        min_idx = self.min_heap.index(x)
        max_idx = self.max_heap.index(-x)
        self.min_heap[min_idx] = self.min_heap[-1]
        self.min_heap.pop()
        self.max_heap[max_idx] = self.max_heap[-1]
        self.max_heap.pop()
        if min_idx < len(self.min_heap):
            heapq._siftup(self.min_heap, min_idx)
            heapq._siftdown(self.min_heap, 0, min_idx)
        if max_idx < len(self.max_heap):
            heapq._siftup(self.max_heap, max_idx)
            heapq._siftdown(self.max_heap, 0, max_idx)

    def getFront(self):
        # Get front element
        return self.queue[0]
    
    def getMin(self):
        # Get minimum element
        return self.min_heap[0]
        
    def getMax(self):
        # Get maximum element
        return -1*self.max_heap[0]
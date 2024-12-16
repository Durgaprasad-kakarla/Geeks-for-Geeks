# A linked list (LL) node 
# to store a queue entry
class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue:
    def __init__(self):
        self.head=None
        self.tail=None
    
    #Function to push an element into the queue.
    def push(self, item): 
        if self.head:
            new_node=Node(item)
            self.tail.next=new_node
            self.tail=new_node
        else:
            self.head=Node(item)
            self.tail=self.head
    
    #Function to pop front element from the queue.
    def pop(self):
        if self.head:
            temp=self.head
            self.head=self.head.next
            if self.head==self.tail and self.head is None:
                self.tail=None
            return temp.data
        return -1


#{ 
 # Driver Code Starts

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyQueue()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
                i=i+1
        print()   
        print("~")
# } Driver Code Ends
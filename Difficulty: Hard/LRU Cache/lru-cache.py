#User function Template for python3

# design the class in the most optimal way
class Node:
    def __init__(self,key,val):
        self.key,self.val=key,val
        self.prev,self.next=None,None
class DLL:
    def __init__(self,head,tail):
        self.head=head
        self.tail=tail
    def insert_after_head(self,key,val,node):
        temp,nex=self.head,self.head.next
        node.prev=temp
        node.next=nex
        temp.next=node
        nex.prev=node
    def delete(self,node):
        pre=node.prev
        nex=node.next
        pre.next=nex
        nex.prev=pre
class LRUCache:
      
    #Constructor for initializing the cache capacity with the given value.  
    def __init__(self, capacity):
        #code here
        self.capacity=capacity
        self.dic={}
        self.head=Node(-1,-1)
        self.tail=Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.dll=DLL(self.head,self.tail)
        
        
    #Function to return value corresponding to the key.
    def get(self, key):
        #code here
        if key in self.dic:
            node=self.dic[key]
            self.dll.delete(node)
            self.dll.insert_after_head(node.key,node.val,node)
            return node.val
        return -1
        
        
    #Function for storing key-value pair.   
    def put(self, key, value):
        #code here
        if key in self.dic:
            node=self.dic[key]
            node.val=value
            self.dll.delete(node)
            self.dll.insert_after_head(node.key,value,node)
        else:
            if len(self.dic)<self.capacity:
                node=Node(key,value)
                self.dll.insert_after_head(key,value,node)
                self.dic[key]=node
            else:
                node=self.tail.prev
                self.dll.delete(self.tail.prev)
                self.dic.pop(node.key)
                node.key,node.val=key,value
                self.dic[key]=node
                self.dll.insert_after_head(key,value,node)




#{ 
 # Driver Code Starts
#Initial Template for Python 3


def inputLine():
    return input().strip().split()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        capacity = int(input())
        cache = LRUCache(capacity)

        queries = int(input())
        for __ in range(queries):
            vec = inputLine()
            if vec[0] == "PUT":
                key = int(vec[1])
                value = int(vec[2])
                cache.put(key, value)
            else:
                key = int(vec[1])
                print(cache.get(key), end=" ")
        print()
        print("~")

# } Driver Code Ends
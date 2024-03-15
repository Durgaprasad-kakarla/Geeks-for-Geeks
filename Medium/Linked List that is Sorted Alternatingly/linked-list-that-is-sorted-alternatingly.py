#User function Template for python3

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class Solution:
    def sort(self, head):
        #return head
        if head.next is None:
            return head
        h1,h2=head,head.next
        dummy1=h1
        dummy2=h2
        dummy1.next=None
        i=0
        while dummy1 and dummy2:
            prev1=dummy1
            prev2=dummy2
            if i%2==0:
                curr=dummy2.next
                dummy2.next=None
                dummy1.next=curr
                dummy1=dummy1.next
            else:
                curr=dummy1.next
                dummy1.next=None
                dummy2.next=curr
                dummy2=dummy2.next
            i+=1
        
        dummy=None
        while h2:
            curr=h2.next
            h2.next=dummy
            dummy=h2
            h2=curr
        final=Node(None)
        temp=final
        h2=dummy
        while h1 and h2:
            if h1.data<h2.data:
                temp.next=Node(h1.data)
                temp=temp.next
                h1=h1.next
            else:
                temp.next=Node(h2.data)
                temp=temp.next
                h2=h2.next
        while h1:
            temp.next=Node(h1.data)
            temp=temp.next
            h1=h1.next
        while h2:
            temp.next=Node(h2.data)
            temp=temp.next
            h2=h2.next
        return final.next


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Llist:
    def __init__(self):
        self.head=None
    
    def insert(self,data,tail):
        node=Node(data)
        
        if not self.head:
            self.head=node
            return node
        
        tail.next=node
        return node
        

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        
        n1=int(input())
        arr1=[int(x) for x in input().split()]
        ll1=Llist()
        tail=None
        for nodeData in arr1:
            tail=ll1.insert(nodeData,tail)
            
        
        ob = Solution()
        resHead=ob.sort(ll1.head)
        printList(resHead)
        print()
        
    
    
# } Driver Code Ends
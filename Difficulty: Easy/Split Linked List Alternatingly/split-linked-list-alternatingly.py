#User function Template for python3
'''
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def alternatingSplitList(self, head):
        #Your code here
        temp,prev1,prev2,cnt,head2,cur=head,head,None,0,None,None
        while temp:
            cur=temp.next
            if cnt%2==0:
                if temp.next:
                    prev1.next=temp.next.next
                else:
                    prev1.next=None
                prev1=prev1.next
            else:
                if prev2:
                    prev2.next=temp
                    prev2=prev2.next
                else:
                    head2=temp
                    prev2=temp
            temp=cur 
            cnt+=1
        if prev2:
            prev2.next=None
        return head,head2
                

#{ 
 # Driver Code Starts
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        head = Node(arr[0])
        tail = head

        for i in range(1, len(arr)):
            tail.next = Node(arr[i])
            tail = tail.next

        ob = Solution()
        result = ob.alternatingSplitList(head)
        printList(result[0])
        printList(result[1])

# } Driver Code Ends
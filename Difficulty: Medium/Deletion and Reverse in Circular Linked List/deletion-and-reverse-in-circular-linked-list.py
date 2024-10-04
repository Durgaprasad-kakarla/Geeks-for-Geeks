#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    # Function to reverse a circular linked list
    def reverse(self, head):
        #code here
        if not head:
            return None
        temp=head
        dummy=None
        cnt=0
        while temp!=head or (temp==head and cnt==0):
            curr=temp.next
            temp.next=dummy
            dummy=temp
            temp=curr
            cnt+=1
        temp.next=dummy
        return dummy
            
            
            
    # Function to delete a node from the circular linked list
    def deleteNode(self, head, key):
        #code here
        if head==head.next:
            return None
        if head.data==key:
            temp=head
            while temp.next!=head:
                temp=temp.next
            temp.next=head.next
            return head.next
        else:
            temp,prev=head,head
            cnt=0
            while temp!=head or (temp==head and cnt==0):
                if temp.data==key:
                    prev.next=temp.next
                    break
                prev=temp
                temp=temp.next
                cnt+=1
            return head
        
        


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(head):
    if head is None:
        print("empty")
        return

    temp = head
    while True:
        print(temp.data, end=" ")
        temp = temp.next
        if temp == head:
            break
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        key = int(input())

        head = Node(arr[0])
        tail = head
        for i in range(1, len(arr)):
            tail.next = Node(arr[i])
            tail = tail.next
        tail.next = head  # Make the list circular

        ob = Solution()
        head = ob.deleteNode(head, key)
        head = ob.reverse(head)
        printList(head)

# } Driver Code Ends
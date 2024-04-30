#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, num1, num2):
        # code here
        # return head of sum list
        def reverse(head):
            dummy=None
            while head:
                curr=head.next
                head.next=dummy
                dummy=head
                head=curr
            return dummy
        head1=reverse(num1)
        head2=reverse(num2)
        dummy=Node(-1)
        temp=dummy
        carry=0
        while head1 or head2 or carry:
            sm=0
            if head1:
                sm+=head1.data
                head1=head1.next
            if head2:
                sm+=head2.data
                head2=head2.next
            sm+=carry
            temp.next=Node(sm%10)
            temp=temp.next
            carry=sm//10
        head=reverse(dummy.next)
        while head and head.data==0:
            head=head.next
        if head is None:
            return Node(0)
        return head


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        num1 = LinkedList()
        for i in arr1:
            num1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        num2 = LinkedList()
        for i in arr2:
            num2.insert(i)
        
        res = Solution().addTwoLists(num1.head, num2.head)
        printList(res)
# } Driver Code Ends
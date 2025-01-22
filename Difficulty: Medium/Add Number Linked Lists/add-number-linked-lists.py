#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def addTwoLists(self, num1, num2):
        # code here
        def reverse(head):
            dummy=None
            while head:
                curr=head.next
                head.next=dummy
                dummy=head
                head=curr
            return dummy
        l1,l2=reverse(num1),reverse(num2)
        head=Node(-1)
        temp,carry=head,0
        while l1 or l2 or carry:
            sm=0
            if l1:
                sm+=l1.data
                l1=l1.next
            if l2:
                sm+=l2.data
                l2=l2.next
            sm+=carry
            temp.next=Node(sm%10)
            carry=sm//10
            temp=temp.next
        head=reverse(head.next)
        while head:
            if head.data==0:
                head=head.next
            else:
                break
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
        print(n.data, end=' ')
        n = n.next
    print()


if __name__ == '__main__':
    for _ in range(int(input())):

        arr1 = (int(x) for x in input().split())
        num1 = LinkedList()
        for i in arr1:
            num1.insert(i)

        arr2 = (int(x) for x in input().split())
        num2 = LinkedList()
        for i in arr2:
            num2.insert(i)

        res = Solution().addTwoLists(num1.head, num2.head)
        printList(res)
        print("~")

# } Driver Code Ends
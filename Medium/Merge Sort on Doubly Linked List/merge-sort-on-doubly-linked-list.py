#User function Template for python3

'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None
'''

class Solution():
#Function to sort the given doubly linked list using Merge Sort.
    def sortDoubly(self,head):
    #Your code here
        def merge(head1,head2):
            dummy=Node(None)
            temp=dummy
            while head1 and head2:
                if head1.data<head2.data:
                    temp.next=head1
                    head1.prev=temp
                    temp=head1
                    head1=head1.next
                else:
                    temp.next=head2
                    head2.prev=temp
                    temp=head2
                    head2=head2.next
            if head1:
                head1.prev=temp
                temp.next=head1
            else:
                head2.prev=temp
                temp.next=head2
            x=dummy.next
            dummy.next.prev=None
            return x
        def find_middle(head):
            slow,fast=head,head.next
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            return slow
        def mergesort(head):
            if head==None or head.next==None:
                return head
            middle=find_middle(head)
            lefthead=head
            righthead=middle.next
            middle.next.prev=None
            middle.next=None
            lefthead=mergesort(lefthead)
            righthead=mergesort(righthead)
            return merge(lefthead,righthead)
        return mergesort(head)
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(1000000)


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def printList(self, node):
        while (node.next is not None):
            node = node.next
        while node.prev is not None:
            node = node.prev
        while (node is not None):
            print(node.data, end=" ")
            node = node.next
        print()


def printList(node):
    temp = node

    while (node is not None):
        print(node.data, end=" ")
        temp = node
        node = node.next
    print()
    while (temp):
        print(temp.data, end=" ")
        temp = temp.prev


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        llist = DoublyLinkedList()
        for e in arr:
            llist.append(e)
        ob = Solution()
        llist.head = ob.sortDoubly(llist.head)
        printList(llist.head)
        print()

# } Driver Code Ends
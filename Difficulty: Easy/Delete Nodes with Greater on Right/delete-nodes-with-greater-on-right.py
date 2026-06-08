'''
Structure of linked list node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''
class Solution:
    def compute(self,head):
        # code here
        def reverse(head):
            dummy=None
            while head:
                curr=head.next
                head.next=dummy
                dummy=head
                head=curr
            return dummy
        head=reverse(head)
        temp=head
        cur=head.next
        last=head
        while cur:
            if temp.data<=cur.data:
                temp.next=cur
                temp=temp.next
                last=temp
            cur=cur.next
        if last:
            last.next=None
        return reverse(head)
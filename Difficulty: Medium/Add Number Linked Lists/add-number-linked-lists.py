'''
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
                

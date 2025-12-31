'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def isPalindrome(self, head):
        # code here
        def reverse(head):
            dummy=None
            while head:
                curr=head.next
                head.next=dummy
                dummy=head
                head=curr
            return dummy
        slow,fast,prev=head,head,head
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        middle=prev
        head2=prev.next
        prev.next=None
        head2=reverse(head2)
        while head and head2:
            if head.data!=head2.data:
                return False
            head=head.next
            head2=head2.next
        return True
        
        
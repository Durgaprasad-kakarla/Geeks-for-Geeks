"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        # code here
        dummy=None
        while head:
            curr=head.next
            head.next=dummy
            head.prev=curr
            dummy=head
            head=curr
        return dummy
        
        
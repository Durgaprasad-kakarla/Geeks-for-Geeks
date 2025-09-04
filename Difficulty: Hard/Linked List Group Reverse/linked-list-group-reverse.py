"""
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""

class Solution:
    def reverse(self,head):
        dummy,last=None,head
        while head:
            curr=head.next
            head.next=dummy
            dummy=head
            head=curr
        return dummy,last
    def print_lst(self,head):
        temp=head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()
    def reverseKGroup(self, head, k):
        # Code here
        temp=head
        prev=None
        cnt=0
        while temp:
            cnt+=1
            next_node=temp.next
            if cnt%k==0 or not temp.next:
                temp.next=None
                if not prev:
                    rev_head,last=self.reverse(head)
                    head=rev_head
                    last.next=next_node
                    prev=last
                else:
                    curr=prev.next
                    prev.next=None
                    rev_head,last=self.reverse(curr)
                    prev.next=rev_head
                    last.next=next_node
                    prev=last
                # self.print_lst(head)
            temp=next_node
        return head
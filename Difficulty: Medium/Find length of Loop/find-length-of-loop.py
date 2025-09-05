'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        #code here
        slow,fast=head,head
        start=None
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                start=slow
                break
        if start==None:
            return 0
        cnt=1
        temp=start.next
        while temp!=start:
            temp=temp.next
            cnt+=1
        return cnt
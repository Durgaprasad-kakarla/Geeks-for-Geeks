'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    def swapKth(self, head, k):
        # code here
        length,temp=0,head
        while temp:
            temp=temp.next
            length+=1
        n=length
        st_temp,st_prev_node,st_next_node=head,None,head.next
        end_temp,end_prev_node,end_next_node=head,None,head.next
        temp,prev=head,None
        cnt=0
        if k==n-k+1 or k>n:
            return head
        while temp:
            cnt+=1
            if cnt==k:
                st_prev_node=prev
                st_temp=temp
                st_next_node=temp.next
            if cnt==n-k+1:
                end_prev_node=prev
                end_temp=temp
                end_next_node=temp.next
            prev=temp
            temp=temp.next
        st_curr=st_temp.data
        st_temp.data=end_temp.data
        end_temp.data=st_curr
        return head
        

'''
class Node:
    def _init_(self, x):
        self.data = x
        self.next = None
'''
import heapq
class Solution:
    def merge_two_lists(self,head1,head2):
        if head1.data<head2.data:
            curr,head=head1,head1
            temp1,temp2=head1.next,head2
        else:
            curr,head=head2,head2
            temp2,temp1=head2.next,head1
        while temp1 and temp2:
            if temp1.data<temp2.data:
                next_node=temp1.next
                curr.next=temp1
                curr=temp1
                temp1=next_node
            else:
                next_node=temp2.next
                curr.next=temp2
                curr=temp2
                temp2=next_node
        while temp1:
            next_node=temp1.next
            curr.next=temp1
            curr=temp1
            temp1=next_node
        while temp2:
            next_node=temp2.next
            curr.next=temp2
            curr=temp2
            temp2=next_node
        return head
    def mergeKLists(self, lists):
        # code here
        heap=[]
        for head in lists:
            temp=head
            while temp:
                heapq.heappush(heap,temp.data)
                temp=temp.next
        if not heap:
            return None
        head=Node(heapq.heappop(heap))
        temp=head
        while heap:
            temp.next=Node(heapq.heappop(heap))
            temp=temp.next
        return head
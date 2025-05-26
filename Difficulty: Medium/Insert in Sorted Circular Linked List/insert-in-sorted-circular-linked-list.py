
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
class Solution:
    def sortedInsert(self, head, data):
        #code here
        new_node=Node(data)
        def length(head):
            cnt=1
            temp=head.next
            while temp:
                if temp==head:
                    break
                cnt+=1
                last=temp
                temp=temp.next
            return cnt,last
        cnt,last=length(head)
        if head.data>=data:
            new_node.next=head
            last.next=new_node
            return new_node
        temp,prev=head.next,head
        cnt-=1
        flag=0
        while cnt>0:
            if data>=prev.data and data<=temp.data:
                next_node=prev.next
                prev.next=new_node
                new_node.next=next_node
                flag=1
                break
            prev=temp
            temp=temp.next
            cnt-=1
        if flag==0:
            last.next=new_node
            new_node.next=head
        return head
        
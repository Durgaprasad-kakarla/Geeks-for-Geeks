'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:
    def segregate(self, head):
        #code here
        temp=head
        cnt_0,cnt_1,cnt_2=0,0,0
        while temp:
            if temp.data==0:
                cnt_0+=1
            elif temp.data==1:
                cnt_1+=1
            else:
                cnt_2+=1
            temp=temp.next
        temp=head
        while temp:
            if cnt_0>0:
                temp.data=0
                cnt_0-=1
            elif cnt_1>0:
                temp.data=1
                cnt_1-=1
            else:
                temp.data=2
                cnt_2-=1
            temp=temp.next
        return head
    
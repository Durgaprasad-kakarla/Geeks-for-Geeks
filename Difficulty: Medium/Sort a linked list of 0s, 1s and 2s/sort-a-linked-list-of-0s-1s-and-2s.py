'''
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}'''
	
class Solution:
    def segregate(self, head):
        #code here
        cnt0,cnt1,cnt2=0,0,0
        temp=head
        while temp:
            if temp.data==0:
                cnt0+=1
            elif temp.data==1:
                cnt1+=1
            else:
                cnt2+=1
            temp=temp.next
        new_head=Node(None)
        temp=new_head
        for i in range(cnt0):
            temp.next=Node(0)
            temp=temp.next
        for i in range(cnt1):
            temp.next=Node(1)
            temp=temp.next
        for i in range(cnt2):
            temp.next=Node(2)
            temp=temp.next
        return new_head.next
    


#{ 
 # Driver Code Starts
# Initial Template for Python 3


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        head = None
        if arr:
            head = Node(arr[0])
            tail = head
            for value in arr[1:]:
                tail.next = Node(value)
                tail = tail.next

        printList(Solution().segregate(head))
        print("~")

# } Driver Code Ends
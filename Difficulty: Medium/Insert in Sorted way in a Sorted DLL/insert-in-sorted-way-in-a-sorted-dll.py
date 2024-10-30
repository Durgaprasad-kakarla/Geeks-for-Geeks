#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
'''
class Solution:
    #Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
        temp=head
        if head.data>x:
            new_node=Node(x)
            new_node.next=head
            head.prev=new_node
            head=new_node
            return head
        f=0
        while temp:
            if temp.data>x:
                new_node=Node(x)
                pre.next=new_node
                new_node.prev=pre
                new_node.next=temp
                temp.prev=new_node
                f=1
                break
            pre=temp
            temp=temp.next
        if f==0:
            new_node=Node(x)
            pre.next=new_node
            new_node.prev=temp
        return head
                
    


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def print_list(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        values = list(map(int, input().strip().split()))
        head = None
        tail = None

        for value in values:
            if head is None:
                head = Node(value)
                tail = head
            else:
                tail.next = Node(value)
                tail.next.prev = tail
                tail = tail.next

        value_to_insert = int(input().strip())
        solution = Solution()
        head = solution.sortedInsert(head, value_to_insert)
        print_list(head)

        print("~")

# } Driver Code Ends
# your task is to complete this function
# Function should return an integer value
# head1 denotes head node of 1st list
# head2 denotes head node of 2nd list

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

class Solution:
    def multiply_two_lists(self, first, second):
        # Code here
        f=0
        while first:
            f=(first.data+f*10)%(10**9+7)
            first=first.next
        s=0
        while second:
            s=(second.data+s*10)%(10**9+7)
            second=second.next
        mul=(f*s)%(10**9+7)
        return mul%(10**9+7)
        



#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def new_node(data):
    return Node(data)


def push(head_ref, new_data):
    new_Node = new_node(new_data)
    new_Node.next = head_ref[0]
    head_ref[0] = new_Node


def reverse(r):
    prev = None
    cur = r[0]
    while cur is not None:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    r[0] = prev


def free_list(Node):
    while Node:
        temp = Node
        Node = Node.next
        del temp


def print_list(Node):
    while Node:
        print(Node.data, end=" ")
        Node = Node.next
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        first, second = [None], [None]
        arr = list(map(int, input().split()))
        for num in arr:
            push(first, num)

        brr = list(map(int, input().split()))
        for num in brr:
            push(second, num)

        reverse(first)
        reverse(second)

        ob = Solution()
        res = ob.multiply_two_lists(first[0], second[0])
        print(res)

# } Driver Code Ends
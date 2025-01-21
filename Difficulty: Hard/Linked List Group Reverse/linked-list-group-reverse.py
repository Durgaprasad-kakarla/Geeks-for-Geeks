"""Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""
class Solution:
    def reverseKGroup(self, head, k):
        # Code here
        def reverse(head):
            prev = None
            while head:
                next_node = head.next
                head.next = prev
                prev = head
                head = next_node
            return prev
        
        def find_kth(head, k):
            temp = head
            while temp and k > 1:
                temp = temp.next
                k -= 1
            return temp
        temp = head
        prev_group_tail = None
        new_head = None
        
        while temp:
            kth_node = find_kth(temp, k)
            if not kth_node:  # Less than k nodes in the current group
                if prev_group_tail:
                    prev_group_tail.next = reverse(temp)
                else:
                    new_head = reverse(temp)
                break
            
            next_group_head = kth_node.next
            kth_node.next = None  # Detach the current group
            reversed_group = reverse(temp)
            
            if not new_head:
                new_head = reversed_group
            if prev_group_tail:
                prev_group_tail.next = reversed_group
            
            prev_group_tail = temp  # `temp` becomes the tail of the reversed group
            temp = next_group_head  # Move to the next group
        
        return new_head
                    
                
            

#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


if __name__ == '__main__':
    t = int(input())  # Number of test cases
    while t > 0:
        llist = LinkedList()

        # Read list values and push them to the LinkedList
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)

        k = int(input())  # Size of the group for reversal
        ob = Solution()
        new_head = ob.reverseKGroup(llist.head, k)
        llist.head = new_head
        llist.printList()  # Print the modified linked list
        t -= 1

        print("~")

# } Driver Code Ends
'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''

class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        def find_loop(head):
            slow=fast=head
            while fast and fast.next:
                prev=slow
                slow=slow.next
                fast=fast.next.next
                if slow==fast:
                    return slow,prev
            return None,None
        slow,prev=find_loop(head)
        if not slow:
            return head
        temp=head
        while slow!=temp:
            prev=slow
            slow=slow.next
            temp=temp.next
        prev.next=None
        return head



#{ 
 # Driver Code Starts
# driver code:


class Node:

    def __init__(self, val):
        self.next = None
        self.data = val


class linkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, num):
        if self.head is None:
            self.head = Node(num)
            self.tail = self.head
        else:
            self.tail.next = Node(num)
            self.tail = self.tail.next

    def isLoop(self):
        if self.head is None:
            return False

        fast = self.head.next
        slow = self.head

        while slow != fast:
            if fast is None or fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next

        return True

    def loopHere(self, position):
        if position == 0:
            return

        walk = self.head
        for _ in range(1, position):
            walk = walk.next
        self.tail.next = walk

    def length(self):
        walk = self.head
        ret = 0
        while walk:
            ret += 1
            walk = walk.next
        return ret


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        arr = tuple(int(x) for x in input().split())
        pos = int(input())
        n = len(arr)
        ll = linkedList()
        for i in arr:
            ll.add(i)
        ll.loopHere(pos)

        Solution().removeLoop(ll.head)

        if ll.isLoop() or ll.length() != n:
            print("false")
            continue
        else:
            print("true")
        print("~")

# } Driver Code Ends
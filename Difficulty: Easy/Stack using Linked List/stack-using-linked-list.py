class MyStack:
    def __init__(self):
        self.head = None
        self.tail = None
        
    #Function to push an integer into the stack.
    def push(self, data):
        if self.head:
            new_node=StackNode(data)
            new_node.next=self.tail
            self.tail=new_node
        else:
            self.head=StackNode(data)
            self.tail=self.head

    #Function to remove an item from top of the stack.
    def pop(self):
        # print(self.tail.data)
        if self.tail:
            ele=self.tail.data
            self.tail=self.tail.next
            if self.tail==self.head and self.tail is None:
                self.head=None
            return ele
        return -1

#{ 
 # Driver Code Starts
class StackNode:

    # Constructor to initialize a node
    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    T = int(data[0])
    idx = 1
    for _ in range(T):
        sq = MyStack()
        line = data[idx].strip()
        nums = list(map(int, line.split()))
        idx += 1
        n = len(nums)
        i = 0
        while i < n:
            QueryType = nums[i]
            i += 1
            if QueryType == 1:
                a = nums[i]
                i += 1
                sq.push(a)
            elif QueryType == 2:
                print(sq.pop(), end=" ")
        print()
        print("~")

# } Driver Code Ends
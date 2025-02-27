class Solution:

    def __init__(self):
        # code here
        self.stack=[]
        self.minStack=[]
        
    # Add an element to the top of Stack
    def push(self, val):
        # code here
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        elif self.minStack and self.minStack[-1]>=val:
            self.minStack.append(val)

    # Remove the top element from the Stack
    def pop(self):
        # code here
        if self.stack:
            node=self.stack.pop()
            if self.minStack and self.minStack[-1]==node:
                self.minStack.pop()

    # Returns top element of Stack
    def peek(self):
        # code here
        if self.stack:
            return self.stack[-1]
        return -1

    # Finds minimum element of Stack
    def getMin(self):
        # code here
        if self.minStack:
            return self.minStack[-1]
        return -1



#{ 
 # Driver Code Starts
# Driver Code
if __name__ == '__main__':
    t = int(input())  # Number of test cases

    for _ in range(t):
        q = int(input())  # Number of queries
        stk = Solution()  # Initialize stack
        results = []

        for _ in range(q):
            query = list(map(int, input().split()))

            if query[0] == 1:
                stk.push(query[1])  # Push operation
            elif query[0] == 2:
                stk.pop()  # Pop operation (no return value)
            elif query[0] == 3:
                results.append(str(stk.peek()))  # Peek operation
            elif query[0] == 4:
                results.append(str(stk.getMin()))  # GetMin operation

        print(" ".join(results))  # Print all results in one line
        print("~")

# } Driver Code Ends
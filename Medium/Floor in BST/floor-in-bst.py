#User function Template for python3

class Solution:
    def floor(self, root, x):
        # Code here
        ans=-1
        while root:
            if root.data<x:
                ans=root.data
                root=root.right
            elif root.data>x:
                root=root.left
            else:
                return root.data
        if ans==-1:
            return -1
        else:
            return ans
''' Time Complexity--O(logn)  
    Space Complexity--O(1)'''

#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def insert(tree, val):
    if(tree==None):
        return Node(val)
    if(val< tree.data):
        tree.left= insert(tree.left, val)
    elif(val > tree.data):
        tree.right= insert(tree.right, val)
    return tree
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        arr= list(map(int, input().split()))
        root = None
        for k in arr:
            root=insert(root, k)
        s=int(input())
        obj = Solution()
        print(obj.floor(root,s))
# } Driver Code Ends

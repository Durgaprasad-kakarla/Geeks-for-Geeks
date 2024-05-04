#User function Template for python3

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


#Function to return a tree created from postorder and inoreder traversals.
class Solution:
    def buildTree(_,inorder, postorder, n):
    # your code here
        dic={}
        def build(poststart,postend,instart,inend):
            if poststart>postend or instart>inend:
                return None
            root=Node(postorder[postend])
            inroot=dic[postorder[postend]]
            numsleft=inroot-instart
            root.left=build(poststart,poststart+numsleft-1,instart,inroot-1)
            root.right=build(poststart+numsleft,postend-1,inroot+1,inend)
            return root
        for i in range(len(inorder)):
            dic[inorder[i]]=i
        root=build(0,n-1,0,n-1)
        return root
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
from collections import  defaultdict

#Contributed by : PranchalK


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())



# Helper function that allocates  
# a new node  
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

# This funtcion is here just to test  
def preOrder(node):
    if node == None:
        return
    print(node.data, end=" ")
    preOrder(node.left)
    preOrder(node.right)
    
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  # number of nodes in tree
        in_order = list(map(int, input().strip().split()))  # parent child info in list
        post_order = list(map(int, input().strip().split()))  # parent child info in list
        ob = Solution()
        preOrder(ob.buildTree(in_order,post_order,n))
        print()


# } Driver Code Ends
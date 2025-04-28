#User function Template for python3
from functools import lru_cache
'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to return the maximum sum of non-adjacent nodes.
    def getMaxSum(self, root):
        #code here
        def getmax(root,flag):
            if not root:
                return 0
            if (root,flag) in dp:
                return dp[(root,flag)]
            if flag==0:
                l=getmax(root.left,1)
                r=getmax(root.right,1)
                k=getmax(root.left,0)
                g=getmax(root.right,0)
                dp[(root,flag)]=max(l+r+root.data,k+g)
                return dp[(root,flag)]
            else:
                k=getmax(root.left,0)
                g=getmax(root.right,0)
                dp[(root,flag)]=k+g
                return dp[(root,flag)]
        dp={}
        return getmax(root,0)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
import sys
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(10**6)


class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Function to Build Tree
def buildTree(s):
    #Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):

            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):

            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == '__main__':
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        ob = Solution()
        print(ob.getMaxSum(root))

        print("~")

# } Driver Code Ends
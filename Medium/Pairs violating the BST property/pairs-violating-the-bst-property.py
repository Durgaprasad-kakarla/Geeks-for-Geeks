
from typing import Optional
from collections import deque
"""

definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def pairsViolatingBST(self, n : int, root : Optional['Node']) -> int:
        # code here
        arr=[]
        def inorder(root):
            if root:
                inorder(root.left)
                arr.append(root.data)
                inorder(root.right)
        inorder(root)
        def mergesort(l,r):
            cnt=0
            if l>=r:
                return cnt
            mid=(l+r)//2
            cnt+=mergesort(l,mid)
            cnt+=mergesort(mid+1,r)
            cnt+=merge(l,mid,r)
            return cnt
        def merge(l,mid,r):
            left,right=l,mid+1
            cnt=0
            lst=[]
            while left<=mid:
                while right<=r and arr[left]>arr[right]:
                    right+=1
                cnt+=(right-(mid+1))
                left+=1
            left,right=l,mid+1
            while left<=mid and right<=r:
                if arr[left]<=arr[right]:
                    lst.append(arr[left])
                    left+=1
                else:
                    lst.append(arr[right])
                    right+=1
            while left<=mid:
                lst.append(arr[left])
                left+=1
            while right<=r:
                lst.append(arr[right])
                right+=1
            for i in range(l,r+1):
                arr[i]=lst[i-l]
            return cnt
        return mergesort(0,len(arr)-1)
        



#{ 
 # Driver Code Starts

class Node:
    def __init__(self,val):
        self.data=val
        self.right=None
        self.left=None

# Function to Build Tree
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip=list(map(str,s.split()))

    # Create the root of the tree
    root=Node(int(ip[0]))
    size=0
    q=deque()

    # Push the root to the queue
    q.append(root)
    size=size+1

    # Starting from the second element
    i=1
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1

        # Get the current node's value from the string
        currVal=ip[i]

        # If the left child is not null
        if(currVal!="N"):

            # Create the left child for the current node
            currNode.left=Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]

        # If the right child is not null
        if(currVal!="N"):

            # Create the right child for the current node
            currNode.right=Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

def inputTree():
    treeString=input().strip()
    root = buildTree(treeString)
    return root
def inorder(root):
    if (root == None):
       return
    inorder(root.left);
    print(root.data,end=" ")
    inorder(root.right)

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        root = inputTree();
        
        obj = Solution()
        res = obj.pairsViolatingBST(n, root)
        
        print(res)
        

# } Driver Code Ends
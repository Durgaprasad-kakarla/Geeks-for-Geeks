# Your task is to complete this function
# function should return true/false or 1/0
class Solution:
    def isDeadEnd(self, root):
        # Code here
        lst=[]
        leaves=[]
        def inorder(root):
            if root:
                inorder(root.left)
                lst.append(root.data)
                if not root.left and not root.right:
                    leaves.append(root.data)
                inorder(root.right)
        inorder(root)
        dic={}
        for i in range(len(lst)):
            if lst[i] not in dic:
                dic[lst[i]]=i
        for i in leaves:
            if i==1:
                return True
        for i in leaves:
            index=dic[i]
            if index-1>0 and index+1<n:
                if lst[index-1]+1==lst[index] and lst[index+1]-1==lst[index]:
                    return True
        return False
#{ 
 # Driver Code Starts

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        elif root.data == node.data:
            return
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def traverseInorder(root):
    if root is not None:
        traverseInorder(root.left)
        print(root.data, end=" ")
        traverseInorder(root.right)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        root = None
        for j in arr:
            if root is None:
                root = Node(j)
            else:
                insert(root, Node(j))
                
        ob = Solution()
        if ob.isDeadEnd(root):
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends
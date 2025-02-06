#User function Template for python3

'''
# Node class
class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''
# Note: Build tree and return root node
class Solution:
    def buildTree(self, inorder, preorder):
        # code here
        def build(instart,inend,prestart,preend):
            if instart>inend or prestart>preend:
                return None
            inroot=index[preorder[prestart]]
            root=Node(inorder[inroot])
            root.left=build(instart,inroot-1,prestart+1,prestart+(inroot-instart))
            root.right=build(inroot+1,inend,prestart+(inroot-instart)+1,preend)
            return root
        index={}
        n=len(inorder)
        for i in range(n):
            index[inorder[i]]=i
        return build(0,n-1,0,n-1)
        
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3


class Node:

    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


def printPostorder(n):
    if n is None:
        return
    printPostorder(n.left)
    printPostorder(n.right)
    print(n.data, end=' ')


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        inorder = [int(x) for x in input().split()]
        preorder = [int(x) for x in input().split()]

        root = Solution().buildTree(inorder, preorder)
        printPostorder(root)
        print()

# } Driver Code Ends
from collections import deque
class Solution:
    def RemoveHalfNodes(self, node):
        #code here
        global root
        root=node
        def postorder(node,parent,d):
            global root
            if node:
                postorder(node.left,node,'L')
                postorder(node.right,node,'R')
                l,r=0,0
                if node.left:
                    l=1
                if node.right:
                    r=1
                if (l==1 and r==0):
                    if d=='L':
                        if parent:
                            parent.left=node.left
                        else:
                            root=node.left
                    else:
                        if parent:
                            parent.right=node.left
                        else:
                            root=node.left
                elif (l==0 and r==1):
                    if d=='L':
                        if parent:
                            parent.left=node.right
                        else:
                            root=node.right
                    else:
                        if parent:
                            parent.right=node.right
                        else:
                            root=node.right
                
        postorder(node,None,'')
        return root
                



#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildTree(s):
    if len(s) == 0 or s[0] == 'N':
        return None

    ip = s.split()
    root = Node(int(ip[0]))

    queue = []
    queue.append(root)

    i = 1
    while len(queue) > 0 and i < len(ip):
        currNode = queue.pop(0)
        currVal = ip[i]

        if currVal != 'N':
            currNode.left = Node(int(currVal))
            queue.append(currNode.left)

        i += 1
        if i >= len(ip):
            break

        currVal = ip[i]

        if currVal != 'N':
            currNode.right = Node(int(currVal))
            queue.append(currNode.right)

        i += 1

    return root


def printInorder(root):
    if root is None:
        return

    printInorder(root.left)
    print(root.data, end=' ')
    printInorder(root.right)


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])
    index = 1

    while t > 0:
        s = data[index]
        root = buildTree(s)
        solution = Solution()
        fresh = solution.RemoveHalfNodes(root)
        printInorder(fresh)
        print()
        t -= 1
        index += 1

# } Driver Code Ends
class Solution:
    def minTime(self, root, target):
        # code here
        def find_parent(root):
            queue=deque()
            queue.append(root)
            parent_dic={}
            target_node=None
            while queue:
                node=queue.popleft()
                if node.data==target:
                    target_node=node
                if node.left:
                    parent_dic[node.left]=node
                    queue.append(node.left)
                if node.right:
                    parent_dic[node.right]=node
                    queue.append(node.right)
            return parent_dic,target_node
        parent_dic,target_node=find_parent(root)
        st=set()
        queue=deque()
        queue.append([target_node,0])
        st.add(target_node)
        maxi=0
        while queue:
            node,d=queue.popleft()
            # print(node.data,d)
            maxi=max(maxi,d)
            if node in parent_dic and parent_dic[node] not in st:
                queue.append([parent_dic[node],d+1])
                st.add(parent_dic[node])
            if node.left and node.left not in st:
                queue.append([node.left,d+1])
                st.add(node.left)
            if node.right and node.right not in st:
                queue.append([node.right,d+1])
                st.add(node.right)
        return maxi
        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque


# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


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


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        line = input()
        target = int(input())
        root = buildTree(line)
        print(Solution().minTime(root, target))

        print("~")

# } Driver Code Ends
#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def merge(self, root1, root2):
        # code here
        nums1=[]
        def inorder(root):
            if root:
                inorder(root.left)
                nums1.append(root.data)
                inorder(root.right)
        inorder(root1)
        nums2=[]
        def inorder(root):
            if root:
                inorder(root.left)
                nums2.append(root.data)
                inorder(root.right)
        inorder(root2)
        m,n=len(nums1),len(nums2)
        i,j=0,0
        merged=[]
        while i<m and j<n:
            if nums1[i]==nums2[j]:
               merged.append(nums1[i])
               merged.append(nums2[j])
               i+=1
               j+=1
            elif nums1[i]<nums2[j]:
                 merged.append(nums1[i])
                 i+=1
            else:
                merged.append(nums2[j])
                j+=1
        while i<m:
            merged.append(nums1[i])
            i+=1
        while j<n:
            merged.append(nums2[j])
            j+=1
        return merged

#{ 
 # Driver Code Starts.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTree(s):
    # Corner Case
    if len(s) == 0 or s[0] == 'N':
        return None
    
    # Creating list of strings from input string after splitting by space
    ip = s.split()
    
    # Create the root of the tree
    root = Node(int(ip[0]))
    
    # Push the root to the queue
    queue = [root]
    
    # Starting from the second element
    i = 1
    while queue and i < len(ip):
        # Get and remove the front of the queue
        currNode = queue.pop(0)
        
        # Get the current node's value from the string
        currVal = ip[i]
        
        # If the left child is not null
        if currVal != "N":
            # Create the left child for the current node
            currNode.left = Node(int(currVal))
            
            # Push it to the queue
            queue.append(currNode.left)
        
        # For the right child
        i += 1
        if i >= len(ip):
            break
        currVal = ip[i]
        
        # If the right child is not null
        if currVal != "N":
            # Create the right child for the current node
            currNode.right = Node(int(currVal))
            
            # Push it to the queue
            queue.append(currNode.right)
        i += 1
    
    return root



def main():
    t = int(input())
    for _ in range(t):
        s = input()
        root1 = buildTree(s)
        s = input()
        root2 = buildTree(s)
        obj = Solution()
        vec = obj.merge(root1, root2)
        print(" ".join(map(str, vec)))

if __name__ == "__main__":
    main()

# } Driver Code Ends
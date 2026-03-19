class Solution:
    def largestBst(self, root):
        # Your code here
        def largest_bst(root):
            global maxi
            if root is None:
                return (float('inf'),-float('inf'),0,'Y')
            if not root.left and not root.right:
                return (root.data,root.data,1,'Y')
            min_left,max_left,cnt_left,flag_left=largest_bst(root.left)
            min_right,max_right,cnt_right,flag_right=largest_bst(root.right)
            # print(root.data,max_left,min_left,max_right,min_right,cnt_left,cnt_right)
            if root.data>max_left and root.data<min_right and flag_left=='Y' and flag_right=='Y':
                maxi=max(maxi,cnt_left+cnt_right+1)
                # print(maxi)
                return (min(root.data,min_left),max(root.data,max_right),cnt_left+cnt_right+1,'Y')
            return (root.data,root.data,0,'N')
            
        global maxi
        maxi=1
        largest_bst(root)
        return maxi
        
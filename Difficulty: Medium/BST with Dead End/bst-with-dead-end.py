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
        n=len(lst)
        dic={}
        for i in range(len(lst)):
            if lst[i] not in dic:
                dic[lst[i]]=i
        for i in leaves:
            index=dic[i]
            if index+1<n and lst[index]==1 and lst[index+1]==2 :
                    return True
            if index-1>0 and index+1<n:
                if lst[index-1]+1==lst[index] and lst[index+1]-1==lst[index]:
                    return True
        return False
class Solution:
    def maxArea(self, mat):
        # code here
        def largest_rectangle(nums):
            stack=[]
            n=len(nums)
            maxi=0
            for i in range(n):
                ind=i
                while stack and stack[-1][1]>nums[i]:
                    maxi=max(maxi,(i-stack[-1][0])*stack[-1][1])
                    ind=stack[-1][0]
                    stack.pop()
                stack.append([ind,nums[i]])
            while stack:
                ind,ele=stack.pop()
                maxi=max(maxi,(n-ind)*ele)
            return maxi
        n=len(mat)
        m=len(mat[0])
        arr=[0]*m
        maxi=0
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    arr[j]=0
                else:  
                    arr[j]+=mat[i][j]
            maxi=max(maxi,largest_rectangle(arr))
        return maxi

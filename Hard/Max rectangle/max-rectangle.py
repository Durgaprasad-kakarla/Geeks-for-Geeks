#User function Template for python3


class Solution:
    def maxArea(self,mat, n, m):
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


#{ 
 # Driver Code Starts
#Initial Template for Python 3



# Driver Code 
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        R,C = map(int, input().strip().split())
        A = []
        for i in range(R):
            line = [int(x) for x in input().strip().split()]
            A.append(line)
        print(Solution().maxArea(A, R, C)) 
	
# This code is contributed 
# by SHUBHAMSINGH10 

# } Driver Code Ends
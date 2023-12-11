# User function Template for Python3
import sys
class Solution:
    def maxGold(self, n, m, mat):
        # code here
        def func(i,j,mat,dp):
            n=len(mat)
            m=len(mat[0])
            if i<0 or j<0 or i>=n or j>=m:
                return sys.maxsize*-1
            if j==m-1:
                return mat[i][j]
            if dp[i][j]!=-1:
                return dp[i][j]
            du=mat[i][j]+func(i-1,j+1,mat,dp)
            dd=mat[i][j]+func(i+1,j+1,mat,dp)
            r=mat[i][j]+func(i,j+1,mat,dp)
            dp[i][j]=max(du,dd,r)
            return dp[i][j]
        maxi=0
        dp=[[-1 for i in range(m)] for j in range(n)]
        for x in range(n):
            maxi=max(maxi,func(x,0,mat,dp))
        return maxi


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        tarr = [int(x) for x in input().split()]
        M = []
        j = 0
        for i in range (n):
            M.append(tarr[j:j + m])
            j = j+m
        
        ob = Solution()
        print(ob.maxGold(n, m, M))
# } Driver Code Ends
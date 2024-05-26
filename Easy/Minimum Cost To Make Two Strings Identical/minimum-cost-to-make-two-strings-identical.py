#User function Template for python3
class Solution:
	def findMinCost(self, x, y, costX, costY):
		# code here
		n,m=len(x),len(y)
        # def LCS(ind1,ind2,dp):
        #     if ind1<0 or ind2<0:
        #         return 0
        #     if dp[ind1][ind2]!=-1:
        #         return dp[ind1][ind2]
        #     if x[ind1]==y[ind2]:
        #         dp[ind1][ind2]=1+LCS(ind1-1,ind2-1,dp)
        #         return dp[ind1][ind2]
        #     dp[ind1][ind2]=max(LCS(ind1-1,ind2,dp),LCS(ind1,ind2-1,dp))
        #     return dp[ind1][ind2]
        dp=[[0 for i in range(m+1)] for j in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if x[i-1]==y[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        length=dp[n][m]
        return (n-length)*costX+(m-length)*costY

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        X, Y, costX, costY = input().split()
        costX = int(costX)
        costY = int(costY)
        ob = Solution()
        ans = ob.findMinCost(X, Y, costX, costY)
        print(ans)

# } Driver Code Ends
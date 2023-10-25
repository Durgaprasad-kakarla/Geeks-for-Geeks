#User function Template for python3

class Solution:
    def knapSack(self, N, W, val, wt):
        # code here
        dp=[[0 for i in range(W+1)]for j in range(N+1)]
        for ind in range(N-1,-1,-1):
            for j in range(W+1):
                l=dp[ind+1][j]
                r=0
                if wt[ind]<=j:
                    r=val[ind]+dp[ind][j-wt[ind]]
                dp[ind][j]=max(l,r)
        return dp[0][W]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends
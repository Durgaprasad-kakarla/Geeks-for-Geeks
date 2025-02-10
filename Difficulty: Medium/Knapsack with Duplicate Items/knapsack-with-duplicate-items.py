#User function Template for python3

class Solution:
    def knapSack(self, val, wt,capacity):
        # code here
        n=len(val)
        dp=[[0 for i in range(capacity+1)] for _ in range(n+1)]
        for ind in range(1,n+1):
            for j in range(1,capacity+1):
                l=0
                if j>=wt[ind-1]:
                    l=val[ind-1]+dp[ind][j-wt[ind-1]]
                r=dp[ind-1][j]
                dp[ind][j]=max(l,r)
        return dp[n][capacity]
        # def knapsack(ind,tot):
        #     if ind<0:
        #         return 0
        #     if dp[ind][tot]!=-1:
        #         return dp[ind][tot]
        #     l=0
        #     if wt[ind]<=tot:
        #         l=val[ind]+knapsack(ind,tot-wt[ind])
        #     r=knapsack(ind-1,tot)
        #     dp[ind][tot]=max(l,r)
        #     return max(l,r)
        # dp=[[-1 for _ in range(capacity+1)] for _ in range(n)]
        # return knapsack(n-1,capacity)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        W = int(input())
        val = list(map(int, input().split()))
        wt = list(map(int, input().split()))

        ob = Solution()
        print(ob.knapSack(val, wt, W))
        print("~")

# } Driver Code Ends
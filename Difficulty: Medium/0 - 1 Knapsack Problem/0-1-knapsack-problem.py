class Solution:
    def knapsack(self, W, val, wt):
        # code here
        def func(ind,W,dp):
            if ind<0:
                return 0
            if dp[ind][W]!=-1:
                return dp[ind][W]
            l=-float('inf')
            if W>=wt[ind]:
                l=val[ind]+func(ind-1,W-wt[ind],dp)
            r=func(ind-1,W,dp)
            dp[ind][W]=max(l,r)
            return max(l,r) 
        dp=[[-1 for i in range(W+1)] for j in range(len(wt))]
        return func(len(wt)-1,W,dp)


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        capacity = int(input())
        values = list(map(int, input().strip().split()))
        weights = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.knapsack(capacity, values, weights))
        print("~")
# } Driver Code Ends
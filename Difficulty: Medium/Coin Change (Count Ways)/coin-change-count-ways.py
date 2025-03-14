class Solution:
    def count(self, coins, sum):
        # code here 
        def count_coins(ind,target):
            if target==0:
                return 1
            if ind<0:
                return 0
            if dp[ind][target]!=-1:
                return dp[ind][target]
            l=0
            if target>=coins[ind]:
                l=count_coins(ind,target-coins[ind])
            r=count_coins(ind-1,target)
            dp[ind][target]=l+r
            return l+r
        n=len(coins)
        dp=[[-1 for _ in range(sum+1)] for _ in range(n)]
        return count_coins(n-1,sum)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        coins = list(map(int, input().strip().split()))
        sum = int(input())
        ob = Solution()
        print(ob.count(coins, sum))

        print("~")

# } Driver Code Ends
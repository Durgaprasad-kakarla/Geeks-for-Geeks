
from typing import List


class Solution:
    def minimumCost(self, n : int, w : int, cost : List[int]) -> int:
        # code here
        def minimum_cost(ind,w,dp):
            if w==0:
                return 0
            if ind<0:
                return float('inf')
            if dp[ind][w]!=-1:
                return dp[ind][w]
            l=minimum_cost(ind-1,w,dp)
            r=float('inf')
            if ind+1<=w and cost[ind]!=-1:
                r=cost[ind]+minimum_cost(ind,w-(ind+1),dp)
            dp[ind][w]=min(l,r)
            return dp[ind][w]
        dp=[[-1 for i in range(w+1)] for j in range(n)]
        cost=minimum_cost(n-1,w,dp)
        return -1 if cost==float('inf') else cost
            



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        w = int(input())

        cost = IntArray().Input(n)

        obj = Solution()
        res = obj.minimumCost(n, w, cost)

        print(res)

# } Driver Code Ends
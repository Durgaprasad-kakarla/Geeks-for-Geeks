
from typing import List


class Solution:
    def countPartitions(self, n : int, d : int, arr : List[int]) -> int:
        # code here
        n=len(arr)
        totSum=sum(arr)
        if (totSum - d) < 0 or (totSum - d) % 2:
            return 0
        target=(totSum-d)//2
        dp=[[0 for i in range(target+1)] for j in range(n)]
        for i in range(n):
            dp[i][0]=1
        if arr[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][0] = 1
        if arr[0] != 0 and arr[0] <= target:
            dp[0][arr[0]] = 1
        for ind in range(1,n):
            for j in range(target+1):
                l=dp[ind-1][j]
                r=0
                if j>=arr[ind]:
                    r=dp[ind-1][j-arr[ind]]
                dp[ind][j]=l+r
        return dp[n-1][target]%(10**9+7)
        
        



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        d = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.countPartitions(n, d, arr)
        
        print(res)
        

# } Driver Code Ends
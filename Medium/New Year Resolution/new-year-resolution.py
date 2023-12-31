
from typing import List

import sys
class Solution:
    def isPossible(self, N : int, arr : List[int]) -> bool:
        # code here
        n=len(arr)
        k=sum(arr)
        prev=[False for i in range(k+1)]
        prev[0]=True
        if arr[0]<=k:
            prev[arr[0]]=True
        
        for ind in range(1,n):
            curr=[False for i in range(k+1)]
            curr[0]=True
            for target in range(1,k+1):
                take=False
                if target-arr[ind]>=0:
                    take=prev[target-arr[ind]]
                nottake=prev[target]
                curr[target]=take or nottake
            prev=curr
        for i in range(k+1):
            if prev[i]:
                if i>0 and (i%20==0 or i%24==0 or i==2024):
                    return True
        return False
        



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
        
        N = int(input())
        
        
        coins=IntArray().Input(N)
        
        obj = Solution()
        res = obj.isPossible(N, coins)
        
        result_val = 1 if res else 0
        print(result_val)

# } Driver Code Ends
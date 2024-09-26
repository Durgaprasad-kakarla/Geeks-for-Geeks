
from typing import List


class Solution:
    def LongestBitonicSequence(self, n : int, arr : List[int]) -> int:
        # code here
        n=len(arr)
        dp1=[1]*n
        for i in range(1,n):
            for j in range(i):
                if arr[i]>arr[j]:
                    dp1[i]=max(dp1[i],dp1[j]+1)
        dp2=[1]*n
        max_len=0
        for i in range(n-2,-1,-1):
            for j in range(i,n):
                if arr[i]>arr[j]:
                    dp2[i]=max(dp2[i],dp2[j]+1)
        for i in range(n):
            if dp1[i]>1 and dp2[i]>1:
                max_len=max(max_len,dp1[i]+dp2[i]-1)
        return max_len



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

        nums = IntArray().Input(n)

        obj = Solution()
        res = obj.LongestBitonicSequence(n, nums)

        print(res)

# } Driver Code Ends
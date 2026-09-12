class Solution:
    def maxProduct(self, arr: list[int], k: int) -> int:
        # code here
        arr.sort()
        ans=float('-inf')
        n=len(arr)
        for left in range(0,k+1,2):
            right=k-left
            prod=1
            for i in range(left):
                prod*=arr[i]
            for i in range(n-right,n,1):
                prod*=arr[i]
            ans=max(prod,ans)
        return ans
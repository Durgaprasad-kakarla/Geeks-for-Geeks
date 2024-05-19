
from typing import List


class Solution:
    def findClosest(self, n : int, k : int, arr : List[int]) -> int:
        # code here
        l,r=0,n-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid]==k:
                return arr[mid]
            elif arr[mid]>k:
                r=mid-1
            else:
                l=mid+1
        if r<0:
            return arr[l]
        if l>n-1:
            return arr[r]
        if abs(arr[r]-k)==abs(arr[l]-k):
            return max(arr[l],arr[r])
        elif abs(arr[r]-k)<abs(arr[l]-k):
            return arr[r]
        return arr[l]
        



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
        
        
        k = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.findClosest(n, k, arr)
        
        print(res)
        

# } Driver Code Ends
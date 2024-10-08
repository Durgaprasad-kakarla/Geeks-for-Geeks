
from typing import List


class Solution:
    def pairsum(self, arr : List[int]) -> int:
        # code here
        max1,max2=-1,-1
        n=len(arr)
        for i in range(n):
            if max1<arr[i]:
                max2=max1
                max1=arr[i]
            elif max2<arr[i]:
                max2=arr[i]
        return max1+max2
        



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

        arr = list(map(int, input().strip().split()))

        obj = Solution()
        res = obj.pairsum(arr)

        print(res)

# } Driver Code Ends
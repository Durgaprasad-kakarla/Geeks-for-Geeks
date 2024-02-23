from typing import List


class Solution:
    def maxProfit(self, n : int, price : List[int]) -> int:
        # code here
        prev=[[0 for i in range(3)] for j in range(2)]
        for ind in range(n-1,-1,-1):
            cur=[[0 for i in range(3)] for j in range(2)]
            for buy in range(2):
                for limit in range(1,3):
                    if buy:
                        cur[buy][limit]=max(-price[ind]+prev[0][limit],prev[1][limit])
                    else:
                        cur[buy][limit]=max(price[ind]+prev[1][limit-1],prev[0][limit])
            prev=cur
        return prev[1][2]



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
        
        
        price=IntArray().Input(n)
        
        obj = Solution()
        res = obj.maxProfit(n, price)
        
        print(res)
        

# } Driver Code Ends
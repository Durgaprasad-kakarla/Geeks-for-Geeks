
import heapq
from typing import List
class Solution:
    def buyMaximumProducts(self, n : int, k : int, price : List[int]) -> int:
        heap=[]
        for i in range(n):
            heapq.heappush(heap,[price[i],i+1])
        tot=0
        while heap:
            x=heapq.heappop(heap)
            ele=x[0]
            cnt=x[1]
            if k-ele*cnt>=0:
                k-=ele*cnt
                tot+=cnt
            else:
                tot+=(k//ele)
                return tot
        return tot



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
        
        n,k = map(int,input().strip().split())
        
        price=IntArray().Input(n)
        
        obj = Solution()
        res = obj.buyMaximumProducts(n, k, price)
        
        print(res)
        

# } Driver Code Ends
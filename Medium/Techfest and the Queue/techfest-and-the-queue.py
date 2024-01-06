
from typing import List


class Solution:
    def sumOfPowers(self, a : int, b : int) -> int:
        # code here
        sieve=[-1]*(b+1)
        sieve[0],sieve[1]=0,0
        i=2
        while i*i<=b:
            if sieve[i]==-1:
                j=i*i
                while j<=b:
                    sieve[j]=i
                    j+=i
            i+=1
        cnt=0
        for i in range(a,b+1):
            x=i
            while x>1:
                x=x//sieve[x]
                cnt+=1
        return cnt
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # def func(n):
        #     cnt=0
        #     i=2
        #     while i*i<=n:
        #         while n%i==0:
        #             n=n//i
        #             cnt+=1
        #         i+=1
        #     if n>=2:
        #         cnt+=1
        #     return cnt
        # tot=0
        # for i in range(a,b+1):
        #     tot+=func(i)
        # return tot
        



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
        
        a=int(input())
        b=int(input())
        
        obj = Solution()
        res = obj.sumOfPowers(a,b)
        
        print(res)
        

# } Driver Code Ends
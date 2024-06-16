
from typing import List


class Solution:
    def getPrimes(self, n : int) -> List[int]:
        # code here
        sieve=[1]*(n+1)
        sieve[0]=0
        sieve[1]=0
        i=2
        while i<=n:
            j=i*i
            if j<=n and sieve[j]==1:
                while j<=n:
                    sieve[j]=0
                    j+=i
            i+=1
        for i in range(2,n+1):
            if sieve[i]==1 and sieve[n-i]==1:
                return [i,n-i]
        return [-1,-1]
        



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

        obj = Solution()
        res = obj.getPrimes(n)

        IntArray().Print(res)

# } Driver Code Ends
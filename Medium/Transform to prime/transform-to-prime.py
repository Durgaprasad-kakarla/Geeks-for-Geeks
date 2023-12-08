#User function Template for python3


import math
class Solution:
    def minNumber(self, arr,n):
        # code here
        def prime(n):
            if n<2:
                return False
            for i in range(2,int(math.sqrt(n))+1):
                if n%i==0:
                    return False
            return True
        n=sum(arr)
        x=n
        while True:
            if prime(x):
                return x-n
            x+=1
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
 #    l=list(map(int,input().split()))
 #    n=l[0]
 #    m=l[1]
    a=list(map(int,input().split()))
   # k = int(input())
  #  b = list(map(int, input().split()))
    ob = Solution()
    ans=ob.minNumber(a,n)
    print(ans)

# } Driver Code Ends
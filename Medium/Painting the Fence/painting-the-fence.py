#User function Template for python3

class Solution:
    def countWays(self,n,k):
        #code here.
        if k==1:
            if n<=2:
                return 1
            return 0
        if n==1:
            return k
        a=k
        b=k*k
        for i in range(n-2):
            c=((a+b)*(k-1))%(10**9+7)
            a=b
            b=c
        return b%(10**9+7)



#{ 
 # Driver Code Starts

#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    x=list(map(int,input().split()))
    n=x[0]
    k=x[1]
    ob = Solution()
    ans=ob.countWays(n,k)
    print(ans)

# } Driver Code Ends
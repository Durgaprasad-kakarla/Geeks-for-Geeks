#User function Template for python3
class Solution:
    def firstElement (self, n):
        # code here 
        if n==1:
            return 1
        a,b=0,1
        for i in range(n-1):
            c=(a+b)%(10**9+7)
            a=b
            b=c
        return c%(10**9+7)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.firstElement(n))
# } Driver Code Ends
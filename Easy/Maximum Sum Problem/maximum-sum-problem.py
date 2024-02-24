#User function Template for python3

class Solution:
    def maxSum(self, n): 
        # code here 
        def func(n):
            if n>=(n//2+n//3+n//4):
                return n
            l=max(n//2,func(n//2))
            r=max(n//3,func(n//3))
            k=max(n//4,func(n//4))
            return l+r+k
        return func(n)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.maxSum(n))
# } Driver Code Ends
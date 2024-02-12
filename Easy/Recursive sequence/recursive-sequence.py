#User function Template for python3

class Solution:
    def sequence(self, n):
        # code here
        x=1
        i=1
        sm=0
        while i<=n:
            prod=1
            for j in range(i):
                prod*=x
                x+=1
            sm+=prod
            i+=1
        return sm%(10**9+7)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.sequence(N))
# } Driver Code Ends
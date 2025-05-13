#User function Template for python3

class Solution:
    def nCr(self, n, r):
        # code here
        ans=1
        for i in range(r):
            ans=(ans*n)//(i+1)
            n-=1
        return ans
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        r = int(input())
        ob = Solution()
        print(ob.nCr(n, r))
        print("~")
# } Driver Code Ends
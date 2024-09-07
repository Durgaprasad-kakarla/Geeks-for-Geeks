#User function Template for python3

class Solution:
    def findNth(self,n):
        #code here
        if n<9:
            return n
        return self.findNth(n//9)*10+n%9


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for i in range(0, t):
    n = int(input())
    obj = Solution()
    s = obj.findNth(n)
    print(s)

# } Driver Code Ends
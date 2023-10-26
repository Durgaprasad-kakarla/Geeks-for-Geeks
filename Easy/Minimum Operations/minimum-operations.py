#User function Template for python3
import sys
class Solution:
    def minOperation(self, n):
        steps=0
        while n!=0:
            if n%2==0:
                n=n//2
            else:
                n-=1
            steps+=1
        return steps
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.minOperation(n))
# } Driver Code Ends
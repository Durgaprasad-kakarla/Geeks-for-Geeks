#User function Template for python3
from collections import deque
class Solution:
    def minSteps(self, d):
        # code here
        n=0
        while ((n*(n+1))//2<d) or ((n*(n+1))//2>=d and ((n*(n+1))//2-d)&1==1):
            n+=1
        return n
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        d = int(input())

        ob = Solution()
        print(ob.minSteps(d))

# } Driver Code Ends
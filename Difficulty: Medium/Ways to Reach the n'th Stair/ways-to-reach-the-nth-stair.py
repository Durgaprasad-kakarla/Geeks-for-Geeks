
class Solution:
    def countWays(self, n):
        # code here
        a,b=0,1
        while n>0:
            c=a+b
            a=b
            b=c
            n-=1
        return c

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob = Solution()
        print(ob.countWays(m))

        print("~")

# } Driver Code Ends
#User function Template for python3
class Solution:
    #Function to find sum of all possible substrings of the given string.
    def sumSubstrings(self,s):
        n=len(s)
        res=[0]*(n+1)
        # code here
        for i in range(n):
            res[i+1]=(res[i]*(10)+(i+1)*(ord(s[i])-ord('0')))%(10**9+7)
        return sum(res)%(10**9+7)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

import sys
sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s = str(input())
        ob=Solution()
        print(ob.sumSubstrings(s))
# } Driver Code Ends
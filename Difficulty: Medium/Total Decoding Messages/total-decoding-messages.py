#User function Template for python3
class Solution:
	def countWays(self, digits):
		# Code here
        def count_msgs(ind):
            if ind==n:
                return 1
            if digits[ind]=='0':
                return 0
            if dp[ind]!=-1:
                return dp[ind]
            cnt=0
            for i in range(ind,min(ind+2,n)):
                if int(digits[ind:i+1])<27:
                    cnt+=count_msgs(i+1)
            dp[ind]=cnt
            return cnt
        n=len(digits)
        dp=[-1 for i in range(n)]
        return count_msgs(0)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        digits = input()
        ob = Solution()
        ans = ob.countWays(digits)
        print(ans)
        print("~")

# } Driver Code Ends
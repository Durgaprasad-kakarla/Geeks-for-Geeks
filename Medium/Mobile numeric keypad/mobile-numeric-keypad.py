#User function Template for python3
class Solution:
	def getCount(self, n):
		# code here
		dic={0:[0,8],1:[1,2,4],2:[1,2,3,5],3:[2,3,6],4:[1,4,5,7],5:[2,4,5,6,8],6:[3,5,6,9],7:[4,7,8],
		    8:[0,7,5,8,9],9:[6,8,9]}
        def func(n,last,dp):
            if n==0:
                return 1
            if dp[n][last]!=-1:
                return dp[n][last]
            cnt=0
            for i in dic[last]:
                cnt+=func(n-1,i,dp)
            dp[n][last]=cnt
            return cnt
        tot=0
        dp=[[-1 for i in range(10)] for j in range(n)]
        for i in range(10):
            tot+=(func(n-1,i,dp))
        return tot

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution()
        ans = ob.getCount(n)
        print(ans)

# } Driver Code Ends
#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def solve(self, n, m, grid):
        # Code here
        def func(r,c1,c2,dp):
            if c1<0 or c2<0 or c1==m or c2==m:
                return 0
            if r==n:
                return 0
            if dp[r][c1][c2]!=-1:
                return dp[r][c1][c2]
            maxi=0
            dc=[-1,0,1]
            for i in range(3):
                for j in range(3):
                    maxi=max(maxi,func(r+1,c1+dc[i],c2+dc[j],dp))
            if c1==c2:
                dp[r][c1][c2]=maxi+grid[r][c1]
                return maxi+grid[r][c1]
            dp[r][c1][c2]=maxi+grid[r][c1]+grid[r][c2]
            return maxi+grid[r][c1]+grid[r][c2]
        dp=[[[-1 for i in range(m)] for j in range(m)] for k in range(n)]
        return func(0,0,m-1,dp)
            

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, m = list(map(int, input().split()))
        grid = [list(map(int, input().split())) for _ in range(n)]
        obj = Solution()
        res = obj.solve(n, m, grid)
        print(res)
        print("~")
# } Driver Code Ends
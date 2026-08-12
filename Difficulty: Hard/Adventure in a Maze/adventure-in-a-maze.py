class Solution:
    def findWays(self, grid):
        # code here
        def find_ways(i,j):
            # print('i',i,j)
            if i==n-1 and j==m-1:
                return (1,grid[i][j])
            if i>=n or j>=m:
                return (0,-float('inf'))
            if dp[i][j]!=-1:
                return dp[i][j]
            if grid[i][j]==1:
                cnt,maxi=find_ways(i,j+1)
                dp[i][j]=(cnt%mod,maxi+grid[i][j])
            elif grid[i][j]==2:
                cnt,maxi=find_ways(i+1,j)
                dp[i][j]= (cnt%mod,maxi+grid[i][j])
            else:
                cnt1,max1=find_ways(i+1,j)
                cnt2,max2=find_ways(i,j+1)
                dp[i][j]= ((cnt1+cnt2)%mod,grid[i][j]+max(max1,max2))
            return dp[i][j]
        n,m=len(grid),len(grid[0])
        mod=10**9+7
        dp=[[-1 for _ in range(m)] for _ in range(n)]
        cnt,maxi= find_ways(0,0)
        return (0,0) if maxi==-float('inf') else (cnt%mod,maxi)
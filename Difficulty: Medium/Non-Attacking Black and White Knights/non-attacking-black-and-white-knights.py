class Solution:
    def numOfWays(self, n: int, m: int) -> int:
        # code here
        dr=[-2,-2,-1,1,2,2,1,-1]
        dc=[-1,1,2,2,1,-1,-2,-2]
        total=0
        for i in range(n):
            for j in range(m):
                cnt=0
                for k in range(8):
                    nrow=i+dr[k]
                    ncol=j+dc[k]
                    if nrow>=0 and nrow<n and ncol>=0 and ncol<m:
                        cnt+=1
                total+=(m*n-cnt-1)
        return total
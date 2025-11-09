class Solution: 
    def chocolatePickup(self, mat): 
        # code here
        def chocolate_pickup(i1,j1,i2,j2):
            if i1==0 and j1==0 and i2==0 and j2==0:
                if mat[i1][j1]==-1:
                    return -float('inf')
                return mat[i1][j1]
            if i1<0 or j1<0 or mat[i1][j1]==-1:
                return -float('inf')
            if i2<0 or j2<0 or mat[i2][j2]==-1:
                return -float('inf')
            if dp[i1][j1][i2][j2]!=-1:
                return dp[i1][j1][i2][j2]
            if i1==i2 and j1==j2:
                tot=mat[i1][j1]
            else:
                tot=mat[i1][j1]+mat[i2][j2]
            a=chocolate_pickup(i1-1,j1,i2-1,j2)
            b=chocolate_pickup(i1,j1-1,i2,j2-1)
            c=chocolate_pickup(i1-1,j1,i2,j2-1)
            d=chocolate_pickup(i1,j1-1,i2-1,j2)
            dp[i1][j1][i2][j2]=tot+max(a,b,c,d)
            return dp[i1][j1][i2][j2]
        n,m=len(mat),len(mat[0])
        dp=[[[[-1 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
        max_pickup=chocolate_pickup(n-1,m-1,n-1,m-1)
        return max_pickup if max_pickup!=-float('inf') else 0
            
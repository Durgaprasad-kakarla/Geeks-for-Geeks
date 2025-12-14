class Solution:
    def prefixSum2D(self, mat, queries):
        # code here 
        n,m=len(mat),len(mat[0])
        pref=[[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                pref[i][j]=pref[i-1][j]+pref[i][j-1]-pref[i-1][j-1]+mat[i-1][j-1]
        ans=[]
        for i1,j1,i2,j2 in queries:
            i1,j1,i2,j2=i1+1,j1+1,i2+1,j2+1
            ans.append(pref[i2][j2]-pref[i1-1][j2]-pref[i2][j1-1]+pref[i1-1][j1-1])
        return ans
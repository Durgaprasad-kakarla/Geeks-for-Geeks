class Solution:
    def balanceSums(self, mat):
        # code here
        maxi,n,m=0,len(mat),len(mat[0])
        for i in range(n):
            sm=0
            for j in range(m):
                sm+=mat[i][j]
            maxi=max(maxi,sm)
            sm=0
            for j in range(m):
                sm+=mat[j][i]
            maxi=max(maxi,sm)
        # print(maxi)
        tot_operations=0
        for i in range(n):
            sm=0
            for j in range(m):
                sm+=mat[i][j]
            tot_operations+=(maxi-sm)
        return tot_operations
            
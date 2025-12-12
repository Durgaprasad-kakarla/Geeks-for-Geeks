class Solution:
    def transpose(self, mat):
        # code here
        n,m=len(mat),len(mat[0])
        for i in range(n):
            for j in range(i+1):
                mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
        return mat
        
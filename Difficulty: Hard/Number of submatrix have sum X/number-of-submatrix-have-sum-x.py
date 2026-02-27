class Solution:
    def countSquare(self, mat, x):
        # code here
        n,m=len(mat),len(mat[0])
        pref=[[0 for _ in range(m+1)] for _ in range(n+1)]
        dic,tot={0:1},0
        for i in range(1,n+1):
            for j in range(1,m+1):
                pref[i][j]=pref[i][j-1]+pref[i-1][j]-pref[i-1][j-1]+mat[i-1][j-1]
        def get_pref_sum(l1,r1,l2,r2):
            return pref[l2][r2]-pref[l2][r1-1]-pref[l1-1][r2]+pref[l1-1][r1-1]
        # print(pref[4][5],pref[4][2],pref[1][5],pref[1][2])
        cnt=0
        for d in range(min(n,m)+1):
            for i in range(1,n+1):
                for j in range(1,m+1):
                    if i-d>0 and j-d>0:
                        if get_pref_sum(i-d,j-d,i,j)==x:
                            # print(i,j,i-d,j-d)
                            cnt+=1
        return cnt
                    
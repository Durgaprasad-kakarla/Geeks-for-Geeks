class Solution:
    def largestSquare(self, mat: list[list[int]], queries: list[list[int]], k: int) -> list[int]:
        # code here
        n,m=len(mat),len(mat[0])
        pref=[[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                pref[i][j]+=pref[i-1][j]+pref[i][j-1]-pref[i-1][j-1]+mat[i-1][j-1]
        def query(l1,r1,l2,r2):
            l1,r1,l2,r2=l1+1,r1+1,l2+1,r2+1
            return pref[l2][r2]-pref[l2][r1-1]-pref[l1-1][r2]+pref[l1-1][r1-1]
        
        ans=[]
        for row,col in queries:
            flag=0
            for i in range(min(n,m),-1,-1):
                l1,r1,l2,r2=row-i,col-i,row+i,col+i
                # print(l1,r1,l2,r2)
                if l1<0 or r1<0:
                    continue
                if l2>=n or r2>=m:
                    continue
                sm=query(l1,r1,l2,r2)
                if sm<=k:
                    ans.append(2*i+1)
                    flag=1
                    break
            if flag==0:
                ans.append(-1)
        return ans  
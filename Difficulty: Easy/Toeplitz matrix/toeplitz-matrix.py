class Solution:
    def isToeplitz(self, mat):
        # code here
        def right_diagonal(row,col):
            st=set()
            while row<n and col<m:
                st.add(mat[row][col])
                row+=1
                col+=1
            return len(st)==1
        for i in range(n):
            if not right_diagonal(i,0):
                return False
        for i in range(1,m):
            if not right_diagonal(0,i):
                return False
        return True
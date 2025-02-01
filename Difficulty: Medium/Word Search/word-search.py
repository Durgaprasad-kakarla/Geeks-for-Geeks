class Solution:
	def isWordExist(self, mat, word):
		#Code here
        n,m=len(mat),len(mat[0])
        def search(row,col,ind):
            if ind==len(word):
                return True
            vis[row][col]=1
            dr=[-1,0,1,0]
            dc=[0,-1,0,1]
            for i in range(4):
                nrow=row+dr[i]
                ncol=col+dc[i]
                if nrow>=0 and nrow<n and ncol>=0 and ncol<m and not vis[nrow][ncol] and mat[nrow][ncol]==word[ind]:
                    if search(nrow,ncol,ind+1):
                        return True
            vis[row][col]=0
            return False
        vis=[[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if mat[i][j]==word[0]:
                    if search(i,j,1):
                        return True
        return False

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for tt in range(T):
        n = int(input())
        m = int(input())
        mat = []
        for i in range(n):
            a = list(input().strip().split())
            b = []
            for j in range(m):
                b.append(a[j][0])
            mat.append(b)
        word = input().strip()
        obj = Solution()
        ans = obj.isWordExist(mat, word)
        if ans:
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends
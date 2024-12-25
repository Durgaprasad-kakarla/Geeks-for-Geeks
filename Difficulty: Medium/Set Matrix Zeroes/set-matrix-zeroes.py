#User function Template for python3
class Solution:
    def setMatrixZeroes(self, mat):
        def set_zeroes(row,col):
            i,j=row,col
            while i<n:
                mat[i][j]=0
                i+=1
            i,j=row,col
            while j<m:
                mat[i][j]=0
                j+=1
            i,j=row,col
            while i>=0:
                mat[i][j]=0
                i-=1
            i,j=row,col
            while j>=0:
                mat[i][j]=0
                j-=1
        n=len(mat)
        m=len(mat[0])
        vis=[[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    vis[i][j]=1
        for i in range(n):
            for j in range(m):
                if vis[i][j]==1 and mat[i][j]==0:
                    set_zeroes(i,j)
        return mat


#{ 
 # Driver Code Starts
import sys

# Position this line where user code will be pasted.
if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()

    idx = 0
    t = int(data[idx])
    idx += 1
    results = []

    for _ in range(t):
        n, m = map(int, data[idx:idx + 2])
        idx += 2
        arr = []
        for i in range(n):
            arr.append(list(map(int, data[idx:idx + m])))
            idx += m

        sol = Solution()
        sol.setMatrixZeroes(arr)

        for row in arr:
            results.append(" ".join(map(str, row)))

        results.append("~")

    sys.stdout.write("\n".join(results) + "\n")

# } Driver Code Ends
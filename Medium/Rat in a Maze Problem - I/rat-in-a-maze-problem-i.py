#User function Template for python3

class Solution:
    def findPath(self, mat, n):
        # code here
        lst=[]
        def func(i,j,st,mat,vis):
            n=len(mat)
            m=len(mat[0])
            if i<0 or j<0 or i>=n or j>=m:
                return 
            if i==n-1 and j==m-1 and mat[i][j]==1:
                lst.append(st)
                return
            if mat[i][j]==1 and not vis[i][j]:
                vis[i][j]=1
                func(i,j+1,st+'R',mat,vis)
                func(i,j-1,st+'L',mat,vis)
                func(i+1,j,st+'D',mat,vis)
                func(i-1,j,st+'U',mat,vis)
                vis[i][j]=0
        vis=[[0 for i in range(len(mat[0]))] for j in range(len(mat))]
        func(0,0,'',mat,vis)
        return lst

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends
#User function Template for python3

class Solution:
    def matrixSum(self, n, m, mat, q, queries):
        # code here
        lst=[]
        for query in queries:
            dis,i,j=query
            sm=0
            if dis==1:
                drow=[-1,-1,0,1,1,1,0,-1]
                dcol=[0,1,1,1,0,-1,-1,-1]
                for x in range(8):
                    nrow=i+drow[x]
                    ncol=j+dcol[x]
                    if nrow>=0 and nrow<n and ncol>=0 and ncol<m:
                        sm+=mat[nrow][ncol]
                lst.append(sm)
            else:
                drow=[-2,-2,-2,-2,-2,-1,0,1,2,2,2,2,2,1,0,-1]
                dcol=[-2,-1,0,1,2,2,2,2,2,1,0,-1,-2,-2,-2,-2]
                for x in range(16):
                    nrow=i+drow[x]
                    ncol=j+dcol[x]
                    if nrow>=0 and nrow<n and ncol>=0 and ncol<m:
                        sm+=mat[nrow][ncol]
                lst.append(sm)
        return lst
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = [[0]*m for x in range(n)]
        for i in range(n):
            arr = input().split()
            for j in range(m):
                mat[i][j] = int(arr[j])
        q = int(input())
        queries = [[0]*3 for x in range(q)]
        for i in range(q):
            a = input().split()
            for j in range(3):
                queries[i][j] = int(a[j])
        
        ob = Solution()
        ans = ob.matrixSum(n, m, mat, q, queries)
        for i in range(q):
            print(ans[i])
# } Driver Code Ends
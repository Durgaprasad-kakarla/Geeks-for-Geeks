class Solution:
    def celebrity(self, mat):
        # code here
        n=len(mat)
        adj=[[] for _ in range(n)]
        ind=-1
        for i in range(n):
            for j in range(n):
                if mat[i][j]:
                    adj[i].append(j)
            if adj[i]==[]:
                ind=i
        if ind==-1:
            return -1
        for i in range(n):
            if i!=ind and ind not in adj[i]:
                    return -1
        return ind


#{ 
 # Driver Code Starts
# Main function to handle input and output
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        M = []
        for _ in range(n):
            M.append(list(map(int, input().split())))

        ob = Solution()
        print(ob.celebrity(M))

# } Driver Code Ends
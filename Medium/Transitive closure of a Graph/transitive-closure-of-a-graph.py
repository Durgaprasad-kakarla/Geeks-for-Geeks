#User function Template for python3

class Solution:
    def transitiveClosure(self, N, graph):
        # code here
        adjlst=[]
        for lst in graph:
            new_lst=[]
            for i in range(len(lst)):
                if lst[i]==1:
                    new_lst.append(i)
            adjlst.append(new_lst)
        transitive_closure=[]
        def dfs(node,vis,adjlst):
            vis[node]=1
            for i in adjlst[node]:
                if not vis[i]:
                    dfs(i,vis,adjlst)
        for i in range(N):
            vis=[0 for i in range(N)]
            dfs(i,vis,adjlst)
            transitive_closure.append(vis)
        return transitive_closure
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        graph = []
        for i in range(0,N):
            graph.append([int(j) for j in input().split()])
        ob = Solution()
        ans = ob.transitiveClosure(N, graph)
        for i in range(N):
            for j in range(N):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends
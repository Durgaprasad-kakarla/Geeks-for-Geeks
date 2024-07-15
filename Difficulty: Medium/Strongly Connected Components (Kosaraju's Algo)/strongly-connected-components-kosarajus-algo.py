#User function Template for python3

class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        # code here
        def dfs(node,vis,adj,stack):
            vis[node]=1
            for i in adj[node]:
                if not vis[i]:
                    dfs(i,vis,adj,stack)
            stack.append(node)
        def depfs(node,vis,adj):
            vis[node]=1
            for i in adj[node]:
                if not vis[i]:
                    depfs(i,vis,adj)
        n=len(adj)
        vis=[0 for i in range(n)]
        stack=[]
        for i in range(n):
            if not vis[i]:
                dfs(i,vis,adj,stack)
        # print(stack)
        rev_adj=[[] for i in range(n)]
        for i in range(n):
            for j in adj[i]:
                rev_adj[j].append(i)
        # print(rev_adj)
        vis=[0 for i in range(n)]
        scc_cnt=0
        while stack:
            node=stack.pop()
            if not vis[node]:
                # print(node)
                depfs(node,vis,rev_adj)
                scc_cnt+=1
        return scc_cnt


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict 
import sys 

sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        print(ob.kosaraju(V, adj))
# } Driver Code Ends
class Solution:

    def kosaraju(self, adj):
        #code here
        def dfs(node,adj):
            vis[node]=1
            for i in adj[node]:
                if not vis[i]:
                    dfs(i,adj)
            stack.append(node)
        def check_dfs(node,adj):
            vis[node]=1
            for i in adj[node]:
                if not vis[i]:
                    check_dfs(i,adj)
        n=len(adj)
        vis=[0]*n
        stack=[]
        for i in range(n):
            if not vis[i]:
                dfs(i,adj)
        rev_adj=[[] for _ in range(n)]
        for i in range(n):
            for j in adj[i]:
                rev_adj[j].append(i)
        # print(stack,rev_adj)
        cnt=0
        vis=[0]*n
        for i in stack[::-1]:
            if not vis[i]:
                check_dfs(i,rev_adj)
                cnt+=1
        return cnt
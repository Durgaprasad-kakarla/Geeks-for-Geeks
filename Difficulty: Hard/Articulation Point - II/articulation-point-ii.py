class Solution:
    def articulationPoints(self, V, edges):
        # code here
        def dfs(node,parent):
            global timer
            vis[node]=1
            tin[node]=low[node]=timer
            timer+=1
            child=0
            for i in adj[node]:
                if i==parent:
                    continue
                if not vis[i]:
                    dfs(i,node)
                    child+=1
                    low[node]=min(low[i],low[node])
                    if low[i]>=tin[node] and parent!=-1:
                        articulation_mark[node]=1
                else:
                    low[node]=min(low[node],tin[i])
            if child>1 and parent==-1:
                articulation_mark[node]=1
        tin=[0]*V
        low=[0]*V
        vis=[0]*V
        articulation_mark=[0]*V
        adj=[[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        global timer
        timer=0
        for i in range(V):
            if not vis[i]:
                dfs(i,-1)
        ans=[]
        for i in range(V):
            if articulation_mark[i]:
                ans.append(i)
        return [-1] if not ans else ans
                    
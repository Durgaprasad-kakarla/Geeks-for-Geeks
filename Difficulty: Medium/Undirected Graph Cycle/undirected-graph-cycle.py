class Solution:
	def isCycle(self, V, edges):
		#Code here
		adj=[[] for _ in range(V)]
		for u,v in edges:
		    adj[u].append(v)
		    adj[v].append(u)
		def dfs(node,parent):
		    vis[node]=1
		    for i in adj[node]:
		        if not vis[i]:
		            if dfs(i,node):
		                return True
		        elif parent!=i:
		            return True
		    return False
		vis=[0 for _ in range(V)]
		for i in range(V):
		    if not vis[i]:
		        if dfs(i,-1):
		            return True
		return False
from collections import deque
class Solution:
	def isCycle(self, V, edges):
		def is_cycle(node,parent):
		    vis[node]=1
		    for i in adj[node]:
		        if not vis[i]:
		            if is_cycle(i,node):
		                return True
		        elif parent!=i:
		            return True
		    return False
		adj=[[] for i in range(V)]
		for u,v in edges:
		    adj[u].append(v)
		    adj[v].append(u)
		vis=[0]*V
		for i in range(V):
		    if not vis[i]:
		        if is_cycle(i,-1):
		            return True
		return False
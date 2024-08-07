from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		def dfs(node,parent):
		    vis[node]=1
		    for i in adj[node]:
		        if not vis[i]:
		            if dfs(i,node):
		                return True
		        elif parent!=i:
		            return True
		    return False
	    vis=[0 for i in range(V)]
	    for i in range(V):
	        if not vis[i]:
	            if dfs(i,-1):
	                return True
	    return False
            


#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
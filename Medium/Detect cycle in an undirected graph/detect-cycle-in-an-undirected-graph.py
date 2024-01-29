from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, n: int, adj: List[List[int]]) -> bool:
		#Code here
        vis=[0]*n
        def bfs(node):
            queue = deque()
            queue.append([node,-1])
            vis[node]=1
            while queue:
                node,parent=queue.popleft()
                for i in adj[node]:
                    if not vis[i]:
                        vis[i]=1
                        queue.append([i,node])
                    elif i!=parent:
                        return True
            return False
        for i in range(n):
            if not vis[i]:
                if bfs(i):
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
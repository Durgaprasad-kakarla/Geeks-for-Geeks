class Solution:

    def findparent(self, vertex, par):
        if vertex == par[vertex]:
            return vertex
        par[vertex] = self.findparent(par[vertex], par)
        return par[vertex]
	def detectCycle(self, n, adj):
		par = [i for i in range(n)]
		depth = [1 for _ in range(n)]
		mp = {}
		for i in range(n):
		    for j in range(len(adj[i])):
		        a = i
		        b = adj[i][j]
                if (a, b) in mp or (b, a) in mp:
                   continue
                mp[(a, b)] = 1
                a_parent = self.findparent(a, par)
                b_parent = self.findparent(b, par)
                if a_parent != b_parent:
                    if depth[a_parent] > depth[b_parent]:
                       par[b_parent] = a_parent
                       depth[a_parent] += depth[b_parent]
                    elif depth[a_parent] < depth[b_parent]:
                       par[a_parent] = b_parent
                       depth[b_parent] += depth[a_parent]
                    else:
                       par[a_parent] = b_parent
                       depth[b_parent] += depth[a_parent]
                else:
                    return 1
        return 0


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
		ans = obj.detectCycle(V, adj)
		print(ans)
# } Driver Code Ends
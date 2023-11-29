class Solution:
	def isEulerCircuitExist(self, V, adj):
		#Code here
		odd,even=0,0
		for i in adj:
		    if len(i)&1==1:
		        odd+=1
		if odd>2:
		    return 0
		elif odd==0:
		    return 2
		else:
		    return 1
#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isEulerCircuitExist(V, adj)
		print(ans)
# } Driver Code Ends
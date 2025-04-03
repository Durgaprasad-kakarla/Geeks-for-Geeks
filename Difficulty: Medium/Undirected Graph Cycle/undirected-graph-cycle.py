
class Solution:
	def isCycle(self, n, edges):
		#Code here
		adj=[[] for i in range(n)]
		for u,v in edges:
		    adj[u].append(v)
		    adj[v].append(u)
		vis=[0 for _ in range(n)]
		def dfs(node,parent):
		    vis[node]=1
		    for i in adj[node]:
		        if not vis[i]:
		            if dfs(i,node):
		                return True
		        elif parent!=i:
		            return True
		    return False
		for i in range(n):
		    if not vis[i]:
		        if dfs(i,-1):
		            return True
		return False
#{ 
 # Driver Code Starts
import sys
#Position this line where user code will be pasted.


def main():
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append((u, v))

        obj = Solution()
        ans = obj.isCycle(V, edges)
        print("true" if ans else "false")
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
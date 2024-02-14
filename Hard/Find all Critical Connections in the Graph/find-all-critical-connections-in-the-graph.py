#User function Template for python3

class Solution:
    def criticalConnections(self, n, adj):
        # code here
        global timer
        timer=1
        def dfs(node,parent,vis,adj,tin,low,bridges):
            global timer
            vis[node]=1
            tin[node]=low[node]=timer
            timer+=1
            for i in adj[node]:
                if i==parent:
                    continue
                if vis[i]==0:
                    dfs(i,node,vis,adj,tin,low,bridges)
                    low[node]=min(low[node],low[i])
                    if low[i]>tin[node]:
                        bridges.append([i,node])
                else:
                    low[node]=min(low[node],low[i])
        vis=[0]*n
        tin=[0]*n
        low=[0]*n
        bridges=[]
        dfs(0,-1,vis,adj,tin,low,bridges)
        new_bridges=[]
        for i in range(len(bridges)):
            new_bridges.append(sorted(bridges[i]))
        new_bridges.sort()
        return new_bridges


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

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
		ans = obj.criticalConnections(V, adj)
		for i in range(len(ans)):
		    print(ans[i][0],ans[i][1])

# } Driver Code Ends
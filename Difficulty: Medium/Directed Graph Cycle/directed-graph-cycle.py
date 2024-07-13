#User function Template for python3
from typing import List


class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        # code here
        def dfs(node,pathvis):
            vis[node]=1
            pathvis[node]=1
            for i in adj[node]:
                if not vis[i]:
                    if dfs(i,pathvis):
                        return True
                elif pathvis[i]:
                    return True
            pathvis[node]=0
            return False
        vis=[0 for i in range(V)]
        pathvis=[0 for i in range(V)]
        for i in range(V):
            if not vis[i]:
                if dfs(i,pathvis):
                    return True
        return False
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V, E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a, b = map(int, input().strip().split())
            adj[a].append(b)
        ob = Solution()

        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)

# } Driver Code Ends
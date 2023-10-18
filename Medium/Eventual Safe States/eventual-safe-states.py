#User function Template for python3

from typing import List

class Solution:    
    def eventualSafeNodes(self, V : int, adj : List[List[int]]) -> List[int]:
        # code here
        def dfscheck(node,graph,vis,pathvis,check):
            vis[node]=1
            pathvis[node]=1
            check[node]=0
            for i in graph[node]:
                if not vis[i]:
                    if dfscheck(i,graph,vis,pathvis,check)==True:
                        check[node]=0
                        return True
                elif pathvis[i]:
                    check[node]=0
                    return True
            check[node]=1
            pathvis[node]=0
            return False
        n=V
        vis=[0]*n
        pathvis=[0]*n
        check=[0]*n
        for i in range(n):
            if not vis[i]:
                dfscheck(i,adj,vis,pathvis,check)
        safenodes=[]
        for i in range(n):
            if check[i]==1:
                safenodes.append(i)
        return safenodes
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
        obj = Solution()
        ans = obj.eventualSafeNodes(V, adj)
        for nodes in ans:
            print(nodes, end = ' ')
        print()
            


# } Driver Code Ends
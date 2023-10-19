#User function Template for python3

class Solution:
    
    #Function to find the level of node X.
    def nodeLevel(self, V, adj, X):
        # code here
        queue=[]
        queue.append([0,0])
        vis=[0]*V
        vis[0]=1
        while queue:
            node=queue.pop(0)
            if node[0]==X:
                return node[1]
            for i in adj[node[0]]:
                if not vis[i]:
                    vis[i]=1
                    queue.append([i,node[1]+1])
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
            adj[b].append(a)
        X=int(input())
        ob = Solution()
        
        print(ob.nodeLevel(V, adj, X))
# } Driver Code Ends

class Solution:
    def isCycle(self, V, edges):
        # code here
        adj=[[] for _ in range(V)]
        indegree=[0 for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
            indegree[v]+=1
        queue=deque()
        for i in range(V):
            if indegree[i]==0:
                queue.append(i)
        topo=[]
        while queue:
            node=queue.popleft()
            topo.append(node)
            for i in adj[node]:
                indegree[i]-=1
                if indegree[i]==0:
                    queue.append(i)
        return not len(topo)==V
        

#{ 
 # Driver Code Starts
from collections import deque


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


if __name__ == "__main__":
    main()

# } Driver Code Ends
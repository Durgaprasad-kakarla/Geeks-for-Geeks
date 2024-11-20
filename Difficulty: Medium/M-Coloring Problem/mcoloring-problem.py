# User function Template for python3

class Solution:
    def graphColoring(self, v, edges, m):
        # code here
        color=[-1]*v
        adj=[[] for i in range(v)]
        for i,j in edges:
            if i!=j:
                adj[i].append(j)
                adj[j].append(i)
        def issafe(node,i,adj):
            for j in adj[node]:
                if color[j]==i:
                    return False
            return True
        def dfs(node,color,adj,n):
            if node==n:
                return True
            for i in range(m):
                if issafe(node,i,adj):
                    color[node]=i
                    if dfs(node+1,color,adj,n):
                        return True
                    color[node]=-1
            return False
        return dfs(0,color,adj,v)
                    
        


#{ 
 # Driver Code Starts
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        edges_input = list(map(int, input().split()))
        m = int(input())
        edges = []

        # Populate the edges list with edge pairs
        for i in range(0, len(edges_input), 2):
            edges.append((edges_input[i], edges_input[i + 1]))

        solution = Solution()
        print("true" if solution.graphColoring(n, edges, m) else
              "false")  # Call the graph coloring function
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
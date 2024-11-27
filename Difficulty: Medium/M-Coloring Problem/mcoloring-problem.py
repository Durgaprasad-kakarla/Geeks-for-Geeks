# User function Template for python3

class Solution:
    def graphColoring(self, v, edges, m):
        # code here
        color=[-1 for i in range(v)]
        adj=[[] for i in range(v)]
        for i,j in edges:
            if i!=j:
                adj[i].append(j)
                adj[j].append(i)
        def issafe(node,col):
            for i in adj[node]:
                if color[i]==col:
                    return False
            return True
        def dfs(node,color):
            if node==v:
                return True
            for i in range(m):
                if issafe(node,i):
                    color[node]=i
                    if dfs(node+1,color):
                        return True
                    color[node]=-1
            return False
        return dfs(0,color)

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
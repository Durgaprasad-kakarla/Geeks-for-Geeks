#User function template for Python

class Solution:
	def shortest_distance(self, adj):
		#Code here
		n=len(adj)
		m=len(adj[0])
		for i in range(n):
		    for j in range(m):
		        if adj[i][j]==-1:
		            adj[i][j]=float('inf')
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    adj[i][j]=min(adj[i][j],adj[i][via]+adj[via][j])
        for i in range(n):
		    for j in range(m):
		        if adj[i][j]==float('inf'):
		            adj[i][j]=-1
        return adj


#{ 
 # Driver Code Starts
#Initial template for Python 

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int, input().split())))
		obj = Solution()
		obj.shortest_distance(matrix)
		for _ in range(n):
			for __ in range(n):
				print(matrix[_][__], end = " ")
			print()
# } Driver Code Ends
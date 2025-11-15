#User function template for Python

class Solution:
	def floydWarshall(self, dist):
		#Code here
		n=len(dist)
		for i in range(n):
		    for j in range(n):
		        if dist[i][j]==10**8:
		            dist[i][j]=float('inf')
		for via in range(n):
		    for i in range(n):
		        for j in range(n):
		            dist[i][j]=min(dist[i][j],dist[i][via]+dist[via][j])
		for i in range(n):
		    for j in range(n):
		        if dist[i][j]==float('inf'):
		            dist[i][j]=10**8
		return dist
		            
		            
		            
		            
		            
		            
		            
		            
		            
		            
		            
#User function Template for python3

class Solution:
	def isEularCircuitExist(self, v, adj):
		#Code here
		cnt=0
		for i in range(v):
		    if adj[i]==[]:
		        cnt+=1
		if cnt==v:
		    return True
        for i in range(v):
            if len(adj[i])!=2:
                return False
        return True

#{ 
 # Driver Code Starts
#Initial Template for python3

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
		ans = obj.isEularCircuitExist(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
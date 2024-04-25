#User function Template for python3
from collections import deque
class Solution:
	def FindExitPoint(self, n, m, matrix):
		# Code here
		dic={'R':'D','D':'L','L':'U','U':'R'}
		queue=deque()
		if matrix[0][0]==0:
		    queue.append([0,1,'R'])
		else:
		    queue.append([1,0,'D'])
		dic2={'R':[0,1],'D':[1,0],'L':[0,-1],'U':[-1,0]}
# 		print(dic2[dic['R']])
# 		return (1,0)
        last=(0,0)
		while queue:
		    row,col,direction=queue.popleft()
		    lst=dic2[dic[direction]]
		    lst1=dic2[direction]
		    if row>=0 and col>=0 and row<n and col<m:
		        last=(row,col)
		        if matrix[row][col]==1:
		            matrix[row][col]=0
		            nrow,ncol=lst[0]+row,lst[1]+col
		            queue.append([nrow,ncol,dic[direction]])
		        else:
		            nrow,ncol=lst1[0]+row,lst1[1]+col
		            queue.append([nrow,ncol,direction])
		    else:
		        break
		return last


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        ob = Solution()
        ans = ob.FindExitPoint(n, m, matrix)
        for _ in ans:
            print(_, end=" ")
        print()

# } Driver Code Ends
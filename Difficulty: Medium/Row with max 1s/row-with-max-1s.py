#User function Template for python3
class Solution:

	def rowWithMax1s(self,arr):
		# code here
		def binary_search(arr):
		    n=len(arr)
		    l,r=0,n-1
		    while l<=r:
		        mid=(l+r)//2
		        if arr[mid]==1:
		            r=mid-1
		        else:
		            l=mid+1
		    return (n-(r+1))
		maxi=0
		ind=-1
		for i in range(len(arr)):
		    cnt_1=binary_search(arr[i])
		    if maxi<cnt_1:
		        maxi=cnt_1
		        ind=i
		return ind


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))

        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]

        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends
import heapq
class Solution:
	def kLargest(self, arr, k):
		# Your code here
		n=len(arr)
		heap=[]
		for i in range(n):
		    heapq.heappush(heap,-arr[i])
		ans=[]
		while k>0 and heap:
		    ans.append(-1*heapq.heappop(heap))
		    k-=1
		return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.kLargest(arr, k)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends
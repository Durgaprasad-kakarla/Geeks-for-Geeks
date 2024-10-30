#User function Template for python3
from collections import Counter
class Solution:
	def countPairsWithDiffK(self,arr, k):
    	# code here
    	dic=Counter(arr)
    	tot=0
    	for i in dic:
    	    if i+k in dic:
    	        tot+=(dic[i]*dic[i+k])
        return tot




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.countPairsWithDiffK(arr, k)
        print(ans)
        print("~")
        tc -= 1

# } Driver Code Ends
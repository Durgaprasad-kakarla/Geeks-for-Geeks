#User function Template for python3
from collections import Counter
class Solution:
	def singleNum(self, arr):
		# Code here
        dic=Counter(arr)
        ans=[]
        for i in dic:
            if dic[i]==1:
                ans.append(i)
        return sorted(ans)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        ans = ob.singleNum(arr)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends
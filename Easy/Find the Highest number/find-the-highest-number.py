#User function Template for python3
from typing import List

class Solution:
	def findPeakElement(self, a):
		# Code here
		n=len(a)
		l,r=0,n-1
		ans=-1
		while l<=r:
		    mid=(l+r)//2
		    ans=max(ans,a[mid])
		    if mid==n-1:
		        return a[mid]
		    elif mid<n-1 and a[mid]<a[mid+1]:
		        l+=1
		    else:
		        r-=1
		return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        ob = Solution()
        ans = ob.findPeakElement(a)
        print(ans)

# } Driver Code Ends
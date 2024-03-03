#User function Template for python3
from functools import cmp_to_key
class Solution:

	def printLargest(self, n, nums):
	    # code here
	    def comp(x,y):
            if x+y>y+x:
                return 1
            elif x==y:
                return 0
            else:
                return -1
        nums=[str(i) for i in nums]
        nums.sort(key=cmp_to_key(comp),reverse=True)
        st="".join(nums).lstrip('0')
        if st:
            return st
        return '0'



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import functools

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(str, input().strip().split()))
        ob = Solution()
        ans = ob.printLargest(n, arr)
        print(ans)
        tc -= 1

# } Driver Code Ends
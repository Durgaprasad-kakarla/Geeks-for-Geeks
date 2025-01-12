
class Solution:
    def maxWater(self, arr):
        # code here
        n=len(arr)
        suff_max=[-1]*n
        suff_max[-1],pref,tot=arr[-1],arr[0],0
        for i in range(n-2,-1,-1):
            suff_max[i]=max(suff_max[i+1],arr[i])
        for i in range(1,n-1):
            pref=max(pref,arr[i])
            mini=min(suff_max[i],pref)
            tot+=(mini-arr[i])
        return tot

#{ 
 # Driver Code Starts
#Initial template for Python 3

import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
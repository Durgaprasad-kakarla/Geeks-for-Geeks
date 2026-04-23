class Solution:
    def canSplit(self, arr):
        #code here
        n,tot=len(arr),sum(arr)
        sm=0
        for i in range(n):
            sm+=arr[i]
            if tot-sm==sm:
                return True
        return False
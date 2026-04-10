class Solution:
    def find3Numbers(self, arr):
        # Code Here
        n=len(arr)
        suff=[0]*n
        suff[-1]=arr[-1]
        for i in range(n-2,-1,-1):
            suff[i]=max(suff[i+1],arr[i])
        mini=float('inf')
        for i in range(n):
            if mini<arr[i] and arr[i]<suff[i]:
                return [mini,arr[i],suff[i]]
            mini=min(mini,arr[i])
        return []
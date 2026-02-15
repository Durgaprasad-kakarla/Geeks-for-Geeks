#User function Template for python3

class Solution:

    def findMinDiff(self, arr,m):

        # code here
        arr.sort()
        n=len(arr)
        mini=float('inf')
        for i in range(n-m+1):
            mini=min(mini,arr[i+m-1]-arr[i])
        return mini
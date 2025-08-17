class Solution:
    def rearrange(self, arr, x):
        # code here
        n=len(arr)
        for i in range(n):
            arr[i]=[abs(x-arr[i]),i,arr[i]]
        arr.sort()
        rearranged=[]
        for i in range(n):
            arr[i]=arr[i][2]
        return rearranged
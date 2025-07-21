class Solution:
    def missingNumber(self, arr):
        # code here
        n=len(arr)
        arr.sort()
        x=1
        for i in range(n):
            if arr[i]>0:
                if x<arr[i]:
                    return x
                elif x==arr[i]:
                    x+=1
        return x
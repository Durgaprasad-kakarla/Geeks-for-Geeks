class Solution:
    def checkElements(self, start, end, arr):
        # code here
        n=len(arr)
        arr.sort()
        for i in range(n):
            if arr[i]==start:
                start+=1
            if start>end:
                return True
        return False
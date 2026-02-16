class Solution:
    def canAttend(self, arr):
        # Code Here
        arr.sort()
        n=len(arr)
        for i in range(1,n):
            if arr[i][0]<arr[i-1][1]:
                return False
        return True
        
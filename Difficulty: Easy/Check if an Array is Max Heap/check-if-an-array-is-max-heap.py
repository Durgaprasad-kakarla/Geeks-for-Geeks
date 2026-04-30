import heapq
class Solution:
    def isMaxHeap(self, arr):
        # code here
        n=len(arr)
        for i in range(1,n):
            if i%2==0:
                ind=(i-1)//2
            else:
                ind=(i)//2
            # print(i,ind)
            if arr[i]>(arr[ind]):
                return False
        return True
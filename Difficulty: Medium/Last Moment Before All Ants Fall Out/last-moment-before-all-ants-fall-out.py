class Solution:
    def getLastMoment(self, n, left, right):
        # code here
        max_time=0
        for i in left:
            max_time=max(max_time,i)
        for i in right:
            max_time=max(max_time,n-i)
        return max_time
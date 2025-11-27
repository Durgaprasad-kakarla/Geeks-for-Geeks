class Solution:
    def subsetXORSum(self, arr):
        # code here
        OR,n=0,len(arr)
        for i in arr:
            OR|=i
        return OR * (2**(n-1))
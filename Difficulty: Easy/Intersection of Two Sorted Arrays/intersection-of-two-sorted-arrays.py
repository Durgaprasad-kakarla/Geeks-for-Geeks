class Solution:
    def intersection(self,a, b):
        # code here
        a=set(a)
        b=set(b)
        return sorted(list(a.intersection(b)))
        
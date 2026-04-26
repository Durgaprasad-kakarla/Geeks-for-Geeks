class Solution:
    def commonElements(self, a, b, c):
        # code here
        return sorted(list(set(a).intersection(set(b)).intersection(set(c))))
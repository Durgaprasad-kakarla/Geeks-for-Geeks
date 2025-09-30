from itertools import permutations
class Solution:
    def uniquePerms(self, arr):
        # code here
        return sorted(list(set(permutations(arr))))
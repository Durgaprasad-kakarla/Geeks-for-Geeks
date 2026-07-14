import math
class Solution:
    def find(self, arr):
        # code here
        x = 0
        for i in arr[::-1]:
            x = math.ceil((x + i) / 2)
        return x
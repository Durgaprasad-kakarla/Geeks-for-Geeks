class Solution:
    def minMen(self, arr):
        #code here 
        n = len(arr)
        coverage = [-1] * n
        for i, a in enumerate(arr):
            if a > -1:
                reach = i + a
                j = max(0, i - a)
                if coverage[j] < reach:
                    coverage[j] = reach
        count = 0
        curr_reach = max_reach = -1
        for i, reach in enumerate(coverage):
            if reach > max_reach:
                max_reach = reach
            if curr_reach < i:
                if max_reach < i:
                    return -1
                else:
                    curr_reach = max_reach
                    count += 1
        return count
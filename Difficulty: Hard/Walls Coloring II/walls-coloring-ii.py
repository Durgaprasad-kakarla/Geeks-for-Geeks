class Solution:
    def minCost(self, costs : list[list[int]]) -> int:
        # code here
        n, m = len(costs), len(costs[0])

        # dp for previous row
        prev = costs[0][:]
    
        for row in range(1, n):
    
            # find smallest and second smallest in prev row
            min1 = float('inf')
            min2 = float('inf')
            min1_col = -1
    
            for col in range(m):
                if prev[col] < min1:
                    min2 = min1
                    min1 = prev[col]
                    min1_col = col
                elif prev[col] < min2:
                    min2 = prev[col]
    
            curr = [0] * m
    
            for col in range(m):
                if col == min1_col:
                    curr[col] = costs[row][col] + min2
                else:
                    curr[col] = costs[row][col] + min1
    
            prev = curr
    
        ans = min(prev)
        return -1 if ans == float('inf') else ans
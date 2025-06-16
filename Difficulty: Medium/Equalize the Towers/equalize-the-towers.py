class Solution:
    def minCost(self, heights, cost):
        # code here
        n=len(heights)
        def compute_cost(h):
            r = 0
            for i in range(len(heights)):
                r += cost[i] * abs(heights[i] - h)
            return r
            
        l, r= min(heights), max(heights)
        while r - l > 2:
            m1 = l + (r-l)//3
            m2 = r - (r-l)//3
            c1, c2 = compute_cost(m1), compute_cost(m2)
            if c1 > c2:
                l = m1
            else:
                r = m2
        
        return min(compute_cost(h) for h in range(l, r + 1))
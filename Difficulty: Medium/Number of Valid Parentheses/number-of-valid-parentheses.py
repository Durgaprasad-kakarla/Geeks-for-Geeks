class Solution:
    def findWays(self, n):
        # code here
        def find_ways(l,r,temp):
            if n%2==0 and l==n//2 and r==n//2:
                return 1
            if l>n//2 or r>n//2:
                return 0
            tot=0
            tot+=find_ways(l+1,r,temp+'(')
            if l>r:
                tot+=find_ways(l,r+1,temp+')')
            return tot
        return find_ways(0,0,'')
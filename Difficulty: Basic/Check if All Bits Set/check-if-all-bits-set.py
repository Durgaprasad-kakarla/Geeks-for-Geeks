class Solution:
    def isBitSet(self, n):
        # code here
        if n==0:
            return False
        flag=False
        for i in range(31,-1,-1):
            if n & (1<<i):
                flag=True
            if flag and not n & (1<<i):
                return False
        return True
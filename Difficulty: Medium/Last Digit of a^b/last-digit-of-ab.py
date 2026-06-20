class Solution:
    def getLastDigit(self, a, b):
        # code here
        n=int(a[-1])
        if b=='0':
            return 1
        return pow(n,int(b),10)
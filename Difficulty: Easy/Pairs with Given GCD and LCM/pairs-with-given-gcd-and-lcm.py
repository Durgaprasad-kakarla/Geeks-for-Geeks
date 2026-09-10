class Solution:
    def pairCount(self, x, y):
        """code here"""
        if y%x!=0:
            return 0
        d=(y//x)
        i=2
        cnt=0
        while i*i<=d:
            if d%i==0:
                cnt+=1
                while (d%i==0):
                    d//=i
            i+=1
        if d>1:
            cnt+=1
        return 1<<cnt
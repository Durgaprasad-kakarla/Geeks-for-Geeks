class Solution:
    def findPosition(self, n):
        # code here
        cnt=0
        for i in range(32):
            if n&(1<<i):
                flag=i
                cnt+=1
        if cnt>1:
            return -1
        return flag+1
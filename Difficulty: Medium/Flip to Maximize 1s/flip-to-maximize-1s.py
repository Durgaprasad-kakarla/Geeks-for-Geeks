class Solution:
    def maxOnes(self, arr):
        # code here
        n=len(arr)
        maxi,sm,cnt=0,0,0
        for i in arr:
            if i==1:
                cnt+=1
                sm-=1
            else:
                sm+=1
            sm=max(sm,0)
            maxi=max(maxi,sm)
        return cnt+maxi
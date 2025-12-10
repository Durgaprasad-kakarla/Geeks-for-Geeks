class Solution:
    def findTwoElement(self, arr):
        # code here
        n=len(arr)
        sm=sum(arr)
        actual_sm=(n*(n+1))//2
        sq_sm=0
        for i in arr:
            sq_sm+=i*i
        actual_sq_sm=(n*(n+1)*(2*n+1))//6
        x=(sq_sm-actual_sq_sm)
        y=(sm-actual_sm)
        add=(x//y)
        sub=y
        repeat=(add+sub)//2
        missing=(add-repeat)
        return [repeat,missing]


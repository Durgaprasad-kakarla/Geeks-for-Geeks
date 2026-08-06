class Solution:
    def countMinOperations(self, arr):
        # code here
        n=len(arr)
        mini=float('inf')
        def find_cnt(n):
            cnt,double=0,0
            while n>0:
                if n%2==0:
                    n//=2
                    double+=1
                else:
                    cnt+=1
                    n-=1
            return cnt,double
        tot,double=0,-float('inf')
        for i in range(n):
            cnt,d=find_cnt(arr[i])
            tot+=cnt
            double=max(double,d)
        return tot+double
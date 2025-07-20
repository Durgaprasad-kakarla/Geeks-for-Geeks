class Solution:
    def countValid(self, n, arr):
        # code here
        st=set(arr)
        def cnt_digits(ind,exist):
            if ind==n:
                return exist
            if dp[ind][exist]!=-1:
                return dp[ind][exist]
            start=0
            if ind==0:
                start=1
            cnt=0
            for i in range(start,10):
                if i in st:
                    cnt+=cnt_digits(ind+1,1)
                else:
                    cnt+=cnt_digits(ind+1,exist)
            dp[ind][exist]=cnt
            return cnt
        dp=[[-1 for i in range(2)] for j in range(n)]
        return cnt_digits(0,0)
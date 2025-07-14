class Solution:
    def cuts(self, s):
        # code 
        def is_powerof_5(s):
            k=len(s)
            ele=0
            for i in range(k-1,-1,-1):
                if s[i]=='1':
                    ele+=2**(k-i-1)
            while ele>1:
                if ele%5==0:
                    ele//=5
                else:
                    return False
            return True
        n=len(s)
        def cutting_string(ind):
            if ind==n:
                return 0
            if dp[ind]!=-1:
                return dp[ind]
            mini=float('inf')
            if s[ind]=='1':
                for i in range(ind+1,n+1):
                    if is_powerof_5(s[ind:i]):
                        mini=min(mini,1+cutting_string(i))
            dp[ind]=mini
            return mini 
        dp=[-1]*n
        minimum_cuts=cutting_string(0)
        return -1 if minimum_cuts==float('inf') else minimum_cuts
        
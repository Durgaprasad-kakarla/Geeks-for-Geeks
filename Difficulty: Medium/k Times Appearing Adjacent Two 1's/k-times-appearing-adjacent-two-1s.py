class Solution:
    def countStrings(self, n, k): 
        # code here 
        dp = {}
        mod = int(1e9)+7
        def solve(i,pairs,last):
            if pairs>k:
                return 0
            if i>=n:
                return 1 if pairs==k else 0
            if (i,pairs,last) in dp:
                return dp[(i,pairs,last)]
            chk1 = solve(i+1,pairs,'0')
            chk2=0
            chk3=0
            if last=='1':
                chk2 = solve(i+1,pairs+1,'1')
            else:
                chk3 =solve(i+1,pairs,'1')
            dp[(i,pairs,last)] = ((chk1 + chk2)%mod + chk3)%mod
            return dp[(i,pairs,last)]
       
        return solve(0,0,'')
class Solution:
    def validGroups(self, s):
        # code here
        n=len(s)
        pref=[0]*(n+1)
        for i in range(1,n+1):
            pref[i]+=pref[i-1]+int(s[i-1])
        # print(pref)
        def valid_groups(ind,prev):
            if ind>=n:
                return 1
            if dp[ind][prev+1]!=-1:
                return dp[ind][prev+1]
            total=0
            for i in range(ind+1,n+1):
                # print(pref[i+1],pref[ind])
                if prev<=(pref[i]-pref[ind]):
                    total+=valid_groups(i,pref[i]-pref[ind])
            dp[ind][prev+1]=total
            return total
        n=len(s)
        dp=[[-1 for _ in range(901)] for _ in range(n)]
        return valid_groups(0,-1)
                    
                
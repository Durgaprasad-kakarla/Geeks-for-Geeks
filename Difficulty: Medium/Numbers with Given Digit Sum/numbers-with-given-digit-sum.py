class Solution:
    def countWays(self, n, target):
        # code here
        def count_ways(ind,flag,sm,prev):
            if ind==n:
                if sm==target:
                    return 1
                return 0
            if dp[ind][flag][sm][prev+1]!=-1:
                return dp[ind][flag][sm][prev+1]
            limit=9
            if flag==0:
                limit=arr[ind]
            cnt=0
            for num in range(limit+1):
                if sm+num>target:
                    break
                if prev==-1 and num==0:
                    continue
                if num<arr[ind]:
                    cnt+=count_ways(ind+1,1,sm+num,arr[ind])
                else:
                    cnt+=count_ways(ind+1,flag,sm+num,arr[ind])
            dp[ind][flag][sm][prev+1]=cnt
            return cnt
        arr=[9 for i in range(n)]
        dp=[[[[-1 for _ in range(11)] for _ in range(target+1)] for _ in range(2)] for _ in range(n)]
        ans=count_ways(0,0,0,-1)
        return -1 if ans==0 else ans
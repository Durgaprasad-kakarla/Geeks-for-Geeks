class Solution:
    def countPartitions(self, arr, diff):
        # code here
        n=len(arr)
        tot=sum(arr)
        if (diff+tot)%2!=0:
            return 0
        target=(diff+tot)//2
        # print(target)
        def func(ind,target):
            if ind==0:
                if target==arr[ind]:
                    if arr[ind]==0:
                        return 2
                    return 1
                if target==0:
                    return 1
                return 0
            if dp[ind][target]!=-1:
                return dp[ind][target]
            l=0
            if target>=arr[ind]:
                l=func(ind-1,target-arr[ind])
            r=func(ind-1,target)
            dp[ind][target]=l+r
            return l+r
        dp=[[-1 for _ in range(target+1)] for _ in range(n)]
        return func(n-1,target)
        # for i in range(n):
        #     dp[i][0]=1
        # for i in range(target+1):
        #     if i==arr[0]:
        #         dp[0][i]=1
        # print(dp)
        # for i in range(1,n):
        #     for j in range(target+1):
        #         if j>=arr[i]:
        #             l=dp[i-1][j-arr[i]]
        #         r=dp[i-1][j]
        #     dp[i][j]=l+r
        # return dp[n-1][target]

class Solution():
    def longestString(self, arr):
        # code here
        n=len(arr)
        mini='z'*10000
        for i in range(n):
            arr[i]=[len(arr[i]),arr[i]]
            mini=min(mini,arr[i][1])
        arr.sort()
        dp=[1]*n
        maxi=0
        for i in range(n):
            for j in range(i):
                if arr[i][1][:-1]==arr[j][1]:
                    dp[i]=max(dp[i],dp[j]+1)
                    if dp[i]>maxi:
                        mini=arr[i][1]
                        maxi=dp[i]
                    elif dp[i]==maxi:
                        mini=min(mini,arr[i][1])
        return mini
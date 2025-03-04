#User function Template for python3

class Solution:
    def maximumPoints(self, arr):
        # Code here
        n=len(arr)
        dp=[[0 for i in range(4)] for j in range(n)]
        for i in range(4):
            maxi=0
            for j in range(3):
                if i!=j:
                    maxi=max(maxi,arr[0][j])
            dp[0][i]=maxi
        for day in range(1,n):
            for i in range(4):
                maxi=0
                for j in range(3):
                    if i!=j:
                        maxi=max(maxi,arr[day][j]+dp[day-1][j])
                dp[day][i]=maxi
        return (dp[n-1][3])
            
        # def func(day,prev):
        #     if day==0:
        #         maxi=0
        #         for i in range(1,4):
        #             if i!=prev:
        #                 maxi=max(maxi,arr[0][i-1])
        #         return maxi
        #     if dp[day][prev]!=-1:
        #         return dp[day][prev]
        #     maxi=0
        #     for i in range(1,4):
        #         if i!=prev:
        #             maxi=max(maxi,arr[day][i-1]+func(day-1,i))
        #     dp[day][prev]=maxi
        #     return maxi
        # dp=[[-1 for i in range(4)] for j in range(n)]
        # return func(n-1,0)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [list(map(int, input().split())) for _ in range(n)]
        ob = Solution()
        print(ob.maximumPoints(arr))
        print("~")
# } Driver Code Ends
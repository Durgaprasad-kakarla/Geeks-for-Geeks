class Solution:
    def equalPartition(self, arr):
        # code here
        n=len(arr)
        if sum(arr)&1:
            return False
        target=sum(arr)//2
        def partition_exists(ind,target):
            if target==0:
                return True
            if ind<0:
                return False
            if dp[ind][target]!=-1:
                return dp[ind][target]
            l=partition_exists(ind-1,target)
            r=False
            if target>=arr[ind]:
                r=partition_exists(ind-1,target-arr[ind])
            dp[ind][target]= l or r
            return l or r
        dp=[[-1 for _ in range(target+1)] for _ in range(n)]
        return partition_exists(n-1,target)

#{ 
 # Driver Code Starts
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        if ob.equalPartition(arr):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends
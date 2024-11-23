#User function Template for python3

class Solution:
    def getMinDiff(self,k, arr):
        # code here
        n=len(arr)
        arr.sort()
        ans=arr[-1]-arr[0]
        mini,maxi=arr[0]+k,arr[-1]-k
        for i in range(1,n):
            curr_mini=min(mini,arr[i]-k)
            curr_maxi=max(maxi,arr[i-1]+k)
            # print(curr_mini,curr_maxi)
            ans=min(ans,curr_maxi-curr_mini)
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.getMinDiff(k, arr)
        print(res)
        print("~")

# } Driver Code Ends
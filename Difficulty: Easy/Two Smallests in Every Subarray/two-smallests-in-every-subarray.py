class Solution:
    def pairWithMaxSum(self, arr):
        #code here
        n=len(arr)
        if n<2:
            return -1
        maxi=0
        for i in range(1,n):
            maxi=max(maxi,arr[i-1]+arr[i])
        return maxi

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")

    t = int(data[0])
    lines = data[1:]

    for line in lines:
        s = list(map(int, line.strip().split()))
        solution = Solution()
        res = solution.pairWithMaxSum(s)
        print(res)

# } Driver Code Ends
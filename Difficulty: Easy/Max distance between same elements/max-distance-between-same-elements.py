class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        # Code here
        n=len(arr)
        dic={}
        maxi=0
        for i in range(n):
            if arr[i] in dic:
                maxi=max(maxi,i-dic[arr[i]])
            else:
                dic[arr[i]]=i
        return maxi



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxDistance(arr))

# } Driver Code Ends
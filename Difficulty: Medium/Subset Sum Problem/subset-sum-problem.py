class Solution:
    def isSubsetSum (self, arr, target):
        # code here 
        n=len(arr)
        prev=[False for i in range(target+1)]
        prev[0]=True
        for i in range(1,n+1):
            curr=[False for _ in range(target+1)]
            curr[0]=True
            for j in range(1,target+1):
                l=False
                if j>=arr[i-1]:
                    l=prev[j-arr[i-1]]
                r=prev[j]
                curr[j]=l or r
            prev=curr
        return prev[target]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(arr, sum) == True:
            print("true")
        else:
            print("false")

        print("~")

# } Driver Code Ends
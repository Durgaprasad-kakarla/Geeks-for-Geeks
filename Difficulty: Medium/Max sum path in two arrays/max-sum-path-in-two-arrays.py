#Your task is to complete this function
#Function should return an integer denoting the required answer
class Solution:
    def maxPathSum(self, arr1, arr2):
        # Code here
        tot=0
        n,m=len(arr1),len(arr2)
        i,j,first,second=0,0,0,0
        while i<n and j<m:
            if arr1[i]<arr2[j]:
                first+=arr1[i]
                i+=1
            elif arr2[j]<arr1[i]:
                second+=arr2[j]
                j+=1
            else:
                tot+=max(first,second)+arr1[i]
                i+=1
                j+=1
                first,second=0,0
        while i<n:
            first+=arr1[i]
            i+=1
        while j<m:
            second+=arr2[j]
            j+=1
        return tot+max(first,second)


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxPathSum(arr1, arr2)
        print(ans)

# } Driver Code Ends
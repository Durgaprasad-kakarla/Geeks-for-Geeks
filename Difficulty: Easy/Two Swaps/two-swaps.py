class Solution:
    def checkSorted(self, arr):
        #code here
        def issorted(arr):
            for i in range(len(arr)):
                if arr[i]!=i+1:
                    return False 
            return True
        n=len(arr)
        if issorted(arr):
            return True
        cnt=0
        for i in range(n):
            if arr[i]!=i+1:
                current=arr[i]
                swapped=arr[arr[i]-1]
                arr[i]=swapped
                arr[current-1]=current
                cnt+=1
        if cnt==2 and issorted(arr):
            return True
        return False


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        arr = list(map(int, input().split()))

        sol = Solution()
        result = sol.checkSorted(arr)
        if result:
            print("true")
        else:
            print("false")

# } Driver Code Ends
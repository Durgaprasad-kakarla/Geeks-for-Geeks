#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
class Solution:
    def removeDuplicates(self, arr):
        # code here 
        n=len(arr)
        x=1
        st=set()
        st.add(arr[0])
        for i in range(1,n):
            if arr[i-1]!=arr[i] and arr[i] not in st:
                arr[x]=arr[i]
                x+=1
                st.add(arr[i])
        return arr[:x]
                
    

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.removeDuplicates(arr)
        print(*ans)
        print("~")
        t -= 1


# } Driver Code Ends
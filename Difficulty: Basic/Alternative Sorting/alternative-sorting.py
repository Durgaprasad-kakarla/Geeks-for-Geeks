class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        arr.sort(reverse=True)
        n=len(arr)
        lst=[0]*n
        l,r=0,n-1
        i=0
        while l<r:
            lst[i]=arr[l]
            lst[i+1]=arr[r]
            l+=1
            r-=1
            i+=2
        if n%2!=0:
            lst[i]=arr[l]
        return lst

#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.alternateSort(arr)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends
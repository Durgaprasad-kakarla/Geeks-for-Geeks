#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def modifyAndRearrangeArr (self, arr) : 
        #Complete the function
        i,n=0,len(arr)
        while i+1<n:
            if arr[i]==arr[i+1]:
                arr[i]+=arr[i]
                arr.pop(i+1)
                arr.append(0)
            i+=1
        l,r=0,0
        while r<n:
            if arr[l]>0:
                l+=1
                r+=1
            else:
                if arr[r]>0:
                    arr[l],arr[r]=arr[r],arr[l]
                    l+=1
                    r+=1
                else:
                    r+=1
        return arr
                


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.modifyAndRearrangeArr(arr)
        print(*ans)
        print("~")
        t -= 1


# } Driver Code Ends
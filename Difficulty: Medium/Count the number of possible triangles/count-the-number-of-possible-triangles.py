#User function Template for python3

class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # code here
        arr.sort()
        n=len(arr)
        res=0
        for i in range(n-1,-1,-1):
            l,r=0,i-1
            while l<r:
                if arr[l]+arr[r]>arr[i]:
                    res+=(r-l)
                    r-=1
                else:
                    l+=1
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.countTriangles(arr))

        print("~")

# } Driver Code Ends
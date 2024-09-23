#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        # code here
        n=len(arr)
        sm=sum(arr)
        sm1=(n*(n+1))//2
        sq_sm=0
        for i in range(n):
            sq_sm+=arr[i]**2
        sq_sm1=(n*(n+1)*(2*n+1))//6
        a=sm-sm1
        b=sq_sm-sq_sm1
        b=b//a
        missing=(a+b)//2
        repeating=missing-a
        return missing,repeating

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1

# } Driver Code Ends
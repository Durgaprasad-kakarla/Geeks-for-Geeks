#User function Template for python3
class Solution:
    def maximumSumSubarray (self,k,Arr,n):
        # code here 
        sm=0
        for i in range(k):
            sm+=Arr[i]
        maxi=sm
        for i in range(k,n):
            sm+=(Arr[i]-Arr[i-k])
            maxi=max(maxi,sm)
        return maxi
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends
class Solution:
	def minJumps(self, arr):
	    # code here
        n=len(arr)
        if arr[0]==0:
            return -1
        if arr[0]>=n-1:
            return 1
        dp=[0]*n
        i,cnt=1,1
        while i<n:
            ind=-1
            maxi=-float('inf')
            for j in range(i,i+arr[i-1]):
                if maxi<arr[j]+j:
                    maxi=arr[j]+j
                    ind=j
            if maxi==-float('inf'):
                return -1
            if maxi>=n-1:
                return cnt+1
            i=ind+1
            cnt+=1
        return cnt
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        # n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr)
        print(ans)
        print("~")
# } Driver Code Ends
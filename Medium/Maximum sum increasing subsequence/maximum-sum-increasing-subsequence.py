#User function Template for python3
class Solution:
	def maxSumIS(self, arr, n):
		# code here
		dp=[arr[i] for i in range(n)]
		for ind in range(n):
		    for prev in range(ind):
		        if arr[prev]<arr[ind]:
		            dp[ind]=max(dp[ind],arr[ind]+dp[prev])
		return max(dp)
		'''next=[0 for i in range(n+1)]
	    for ind in range(n-1,-1,-1):
	        cur=[0 for i in range(n+1)]
	        for prev in range(ind-1,-2,-1):
	            l=next[prev+1]
                r=0
                if prev==-1 or (arr[prev]<arr[ind]):
                    r=arr[ind]+next[ind+1]
                cur[prev+1]=max(l,r)
            next=cur
        return cur[0]'''
        '''def func(ind,prev,arr,dp):
            if ind==len(arr):
                return 0
            if dp[ind][prev+1]!=-1:
                return dp[ind][prev+1]
            l=func(ind+1,prev,arr,dp)
            r=0
            if prev==-1 or (arr[prev]<arr[ind]):
                r=arr[ind]+func(ind+1,ind,arr,dp)
            dp[ind][prev+1]=max(l,r)
            return max(l,r)
        dp=[[-1 for i in range(n+1)]for j in range(n)]
        return func(0,-1,Arr,dp)'''

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxSumIS(Arr,n)
		print(ans)

# } Driver Code Ends
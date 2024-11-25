#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		# code here
		pref,suff=1,1
		n=len(arr)
		maxi=-float('inf')
		for i in range(n):
		    pref=pref*arr[i]
		    suff=suff*arr[n-i-1]
		    if pref==0:
    		    pref=1
    		    maxi=max(maxi,0)
    		else:
		        maxi=max(maxi,pref)
		    if suff==0:
		       suff=1
		       maxi=max(maxi,0)
		    else:
		        maxi=max(maxi,suff)
		return maxi
		    
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends
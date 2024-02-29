#User function Template for python3
class Solution:

	
	def sumBitDifferences(self,arr, n):
    	# code here
    	tot=0
    	for i in range(32):
    	    cnt1,cnt0=0,0
    	    for j in range(n):
    	        if (arr[j]>>i)&1==1:
    	            cnt1+=1
    	        else:
    	            cnt0+=1
	        if cnt1>0 and cnt0>0:
	           tot+=(cnt1)*(cnt0)
        return tot*2


#{ 
 # Driver Code Starts

#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.sumBitDifferences(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
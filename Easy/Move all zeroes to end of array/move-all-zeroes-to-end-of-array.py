#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr, n):
    	# code here
    	l,r=0,1
        while l<r and r<n:
            if arr[l]==0:
                if arr[r]==0:
                    r+=1
                else:
                    arr[l],arr[r]=arr[r],arr[l]
                    l+=1
                    r+=1
            else:
                l+=1
                r+=1
        return arr
                    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends
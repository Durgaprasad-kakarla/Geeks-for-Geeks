#User function Template for python3
class Solution:

	def checkTriplet(self,arr, n):
    	# code here
        arr=list(set(arr))
        n=len(arr)
        for i in range(n):
            arr[i]=arr[i]*arr[i]
        for i in range(n):
            for j in range(i-1,-1,-1):
                if arr[i]+arr[j] in arr:
                    return True
        return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.checkTriplet(arr, n)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1

# } Driver Code Ends
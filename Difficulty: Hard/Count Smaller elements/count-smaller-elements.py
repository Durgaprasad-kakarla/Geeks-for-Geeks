#User function Template for python3
class Solution:

	def constructLowerArray(self,arr):
		# code here
		n=len(arr)
		smaller=[0]*n
		def merge(l,r,mid,arr):
		    low,high=l,mid+1
		    i,j=l,mid+1
		    while i<=mid:
		        while j<=r and arr[i][0]>arr[j][0]:
		            j+=1
		        smaller[arr[i][1]]+=(j-(mid+1))
		        i+=1
		    lst=[]
		    while low<=mid and high<=r:
		        if arr[low][0]<=arr[high][0]:
		            lst.append(arr[low])
		            low+=1
		        else:
		            lst.append(arr[high])
		            high+=1
		    while low<=mid:
		        lst.append(arr[low])
		        low+=1
		    while high<=r:
		        lst.append(arr[high])
		        high+=1
		    for i in range(l,r+1):
		        arr[i]=lst[i-l]
		
		def mergesort(l,r,arr):
		    if l>=r:
		        return 
		    mid=(l+r)//2
		    mergesort(l,mid,arr)
		    mergesort(mid+1,r,arr)
		    merge(l,r,mid,arr)
		for i in range(n):
		    arr[i]=[arr[i],i]
		mergesort(0,n-1,arr)
		return smaller
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.constructLowerArray(arr)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
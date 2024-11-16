#User function Template for python3
class Solution:
	def subsetSums(self, arr, n):
		# code here
		def subsetsum(ind,sm):
		    if ind==len(arr):#if index reaches the length of the array append the sum to the subsets
		        subsets.append(sm)
		        return 
		    #pick the element
		    subsetsum(ind+1,sm+arr[ind])
		    # Not picking the element
		    subsetsum(ind+1,sm)
		    
        subsets=[]
        subsetsum(0,0)
        return subsets
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x, end=" ")
        print("")

# } Driver Code Ends
#User function Template for python3

class Solution:
	def canPair(self, nums, k):
		# Code here
		n=len(nums)
		for i in range(n):
		    nums[i]=nums[i]%k
		dic={}
		for i in nums:
		    if i in dic:
		        dic[i]+=1
		    else:
		        dic[i]=1
		if 0 in dic:
		    if dic[0]%2==0:
		        del dic[0]
		    else:
		        return False
		for i in dic:
		    if i==k-i:
		        if dic[i]%2!=0:
		            return False
		    if k-i not in dic or  dic[i]!=dic[k-i]:
		        return False
		return True
		
		            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, k = input().split()
		n = int(n)
		k = int(k)
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.canPair(nums, k)
		if(ans):
			print("True")
		else:
			print("False")
# } Driver Code Ends
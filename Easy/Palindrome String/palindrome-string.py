#User function Template for python3
class Solution:
	def isPalindrome(self, s):
		# code here
		return 1 if s==s[::-1] else 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPalindrome(S)
		print(answer)

# } Driver Code Ends
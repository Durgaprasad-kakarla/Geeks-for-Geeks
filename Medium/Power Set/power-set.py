#User function Template for python3

class Solution:
	def AllPossibleStrings(self, s):
		# Code here
		n=len(s)
		ans=[]
		def subsequence(ind,st):
		    if ind==n:
		        ans.append(st)
		        return 
		    subsequence(ind+1,st)
		    subsequence(ind+1,st+s[ind])
		subsequence(0,'')
	    return sorted(ans)[1:]


#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends
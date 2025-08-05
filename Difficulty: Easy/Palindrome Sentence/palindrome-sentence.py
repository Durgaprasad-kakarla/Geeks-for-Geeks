class Solution:
	def isPalinSent(self, s):
		# code here
		st=''
		n=len(s)
		for i in s:
		    if i.isalnum():
		        st+=i.upper()
		return st==st[::-1]
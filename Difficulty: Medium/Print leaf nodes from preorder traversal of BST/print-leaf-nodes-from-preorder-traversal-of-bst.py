class Solution:
	def leafNodes(self, preorder):
		# code here
		n=len(preorder)
		def func(start,end):
		    if start>end:
		        return 
		    if start==end:
		        ans.append(preorder[start])
		        return 
		    left=start+1
		    while left<n and preorder[start]>preorder[left]:
		        left+=1
		    if left!=start+1:
		        func(start+1,left-1)
		    func(left,end)
		ans=[]
		func(0,n-1)
		return ans
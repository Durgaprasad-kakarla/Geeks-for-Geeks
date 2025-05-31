class Solution:
	def countPairs(self, mat1, mat2, x):
		# code here
		dic={}
		n1,m1=len(mat1),len(mat1[0])
		for i in range(n1):
		    for j in range(m1):
		        dic[mat1[i][j]]=1
		n2,m2=len(mat2),len(mat2[0])
		cnt=0
		for i in range(n2):
		    for j in range(m2):
		        if x-mat2[i][j] in dic:
		            cnt+=1
	    return cnt
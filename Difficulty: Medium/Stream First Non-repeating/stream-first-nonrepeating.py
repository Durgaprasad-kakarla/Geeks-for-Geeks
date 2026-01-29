from collections import deque
class Solution:
	def firstNonRepeating(self, s):
		# code here
		queue=deque()
		n=len(s)
		dic,ans={},''
		for i in range(n):
		    if s[i] in dic:
		        dic[s[i]]+=1
		    else:
		        dic[s[i]]=1
		        queue.append(s[i])
		    while queue and dic[queue[0]]>1:
		        queue.popleft()
		    if queue:
		        ans+=queue[0]
		    else:
		        ans+='#'
		return ans
		        
		
from functools import cmp_to_key
class Solution:
	def findLargest(self, arr):
	    
	    def comp(x,y):
	        if x+y>y+x:
	            return 1
	        elif x==y:
	            return 0
	        return -1
	    arr=[str(i) for i in arr]
	    arr.sort(key=cmp_to_key(comp),reverse=True)
	    st="".join(arr).lstrip('0')
	    return st if st!='' else '0'
class Solution:
	def andInRange(self, l, r):
		# code here
		def previous_power_2(ele):
            x=0
            while 2**x<=ele:
                x+=1
            return 2**(x-1)
        x,y=previous_power_2(l),previous_power_2(r)
        if x!=y:
            return 0
		tot,diff=0,r-l
		curr=0
		for i in range(32):
		    curr+=2**i
		    if (l&(1<<i)):
		        curr-=2**i
		        if diff<=curr:
		            tot+=2**i
		return tot
from collections import defaultdict
class Solution:
	def maxKPower(self, n, k):
	    def cnt_of_each_element(b,k):
	        for i in prime_factors:
	            n=b
	            while n%i==0:
	                current[i]+=1
	                n//=i
		tot=0
		prime_factors=defaultdict(int)
		b,i=k,2
		while i*i<=b:
		    while b%i==0:
		        prime_factors[i]+=1
		        b//=i
		    i+=1
		if b>1:
		    prime_factors[b]+=1
	    current=defaultdict(int)
		for i in range(2,n+1):
		    cnt_of_each_element(i,k)
		mini=float('inf')
		for i in prime_factors:
		    if prime_factors[i]>0:
		        mini=min(mini,current[i]//prime_factors[i])
		return mini
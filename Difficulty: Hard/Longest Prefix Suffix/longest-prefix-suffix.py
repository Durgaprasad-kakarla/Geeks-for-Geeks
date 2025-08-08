class Solution:
	def getLPSLength(self, s):
		# code here
		n=len(s)
        lps=[0]*n
        i,length=1,0
        while i<n:
            if s[i]==s[length]:
                lps[i]=length+1
                length+=1
                i+=1
            else:
                if length!=0:
                    length=lps[length-1]
                else:
                    lps[i]=0
                    i+=1
        return lps[-1]
    		
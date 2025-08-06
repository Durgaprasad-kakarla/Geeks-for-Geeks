class Solution:
    def romanToDecimal(self, s): 
        # code here
        roman_to_int={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        previous_romans='IXC'
        current_romans='VLDM'
        integer=0
        n=len(s)
        i=n-1
        while i>=0:
            if i-1>=0 and s[i-1] in previous_romans and roman_to_int[s[i]]>roman_to_int[s[i-1]]:
                integer+=(roman_to_int[s[i]]-roman_to_int[s[i-1]])
                i-=2
            else:
                integer+=(roman_to_int[s[i]])
                i-=1
            # print(integer,i)
        return integer
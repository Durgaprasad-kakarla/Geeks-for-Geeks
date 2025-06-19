class Solution:
    def caseSort(self,s):
        #code here
        lower,upper=[],[]
        for i in s:
            if ord(i)<97:
                upper.append(i)
            else:
                lower.append(i)
        upper.sort()
        lower.sort()
        sorted_str=""
        j,k=0,0
        for i in s:
            if ord(i)<97:
                sorted_str+=upper[j]
                j+=1
            else:
                sorted_str+=lower[k]
                k+=1
        return sorted_str
class Solution:
    def hIndex(self, citations):
        #code here
        citations.sort()
        n=len(citations)
        maxi=0
        i,j=1,0
        while i<n+1 and j<n:
            if citations[j]==0:
                j+=1
                continue
            elif i<=citations[j]:
                if (n-j)>=i:
                    maxi=max(maxi,i)
                    i+=1
                else:
                    j+=1
            else:
                j+=1
        return maxi

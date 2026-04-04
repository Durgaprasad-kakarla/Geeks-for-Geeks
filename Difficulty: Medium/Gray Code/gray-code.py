class Solution:
    def graycode(self,n):
        #code here
        binary=['0','1']
        for i in range(2,n+1):
            k=len(binary)
            new_binary=[]
            for j in range(k):
                new_binary.append('0'+binary[j])
            for j in range(k-1,-1,-1):
                new_binary.append('1'+binary[j])
            binary=new_binary.copy()
        return binary
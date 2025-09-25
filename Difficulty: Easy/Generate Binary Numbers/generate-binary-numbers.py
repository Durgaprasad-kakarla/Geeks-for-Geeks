class Solution:
    def generateBinary(self, n):
        # code here
        def get_binary(n):
            s=''
            while n>0:
                s=str(n%2)+s
                n//=2
            return s
        binary_lst=[]
        for i in range(1,n+1):
            binary_lst.append(get_binary(i))
        return binary_lst
        
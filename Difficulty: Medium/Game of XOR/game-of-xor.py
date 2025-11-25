class Solution:
    def subarrayXor(self, A):
        # code here 
        N=len(A)
        if N&1==0:
            return 0
        xor=0
        for i in range(N):
            if i%2==0:
                xor=xor^A[i]
        return xor
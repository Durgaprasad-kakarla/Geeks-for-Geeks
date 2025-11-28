class Solution:
    def subsetXOR(self, n : int):
        # code here
        if n%4==0:
            return [i+1 for i in range(n)]
        elif n%4==1:
            return [i+1 for i in range(n-2)]+[n]
        elif n%4==2:
            return [i+1 for i in range(1,n)]
        else:
            return [i+1 for i in range(n-1)]
        

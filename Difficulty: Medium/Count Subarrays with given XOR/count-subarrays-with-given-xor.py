class Solution:
    def subarrayXor(self, arr, k):
        # code here
        dic={0:1}
        n,xor,tot=len(arr),0,0
        for i in range(n):
            xor^=arr[i]
            if xor^k in dic:
                tot+=dic[xor^k]
            if xor in dic:
                dic[xor]+=1
            else:
                dic[xor]=1
        return tot
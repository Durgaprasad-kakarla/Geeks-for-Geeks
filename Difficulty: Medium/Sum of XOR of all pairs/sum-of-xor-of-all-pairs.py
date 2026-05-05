class Solution:
    def sumXOR(self, arr):
        # code here
        n=len(arr)
        cnt_0=[0]*32
        cnt_1=[0]*32
        tot=0
        for i in range(n-1,-1,-1):
            for j in range(32):
                if arr[i]&(1<<j):
                    if cnt_0[j]>0:
                        tot+=(2**j)*cnt_0[j]
                else:
                    if cnt_1[j]>0:
                        tot+=(2**j)*cnt_1[j]
            for j in range(32):
                if arr[i]&(1<<j):
                    cnt_1[j]+=1
                else:
                    cnt_0[j]+=1
        return tot
            
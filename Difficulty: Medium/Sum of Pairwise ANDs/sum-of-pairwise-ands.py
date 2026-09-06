class Solution:
    def pairAndSum(self, arr):
        # code here
        n=len(arr)
        sm=0
        lst=[0]*32
        for i in range(n):
            for j in range(32):
                if (1<<j)&arr[i]:
                    lst[j]+=1
        for i in range(len(lst)):
            x=lst[i]-1
            if x>0:
                sm+=(x*(x+1))//2*(2**i)
        return sm

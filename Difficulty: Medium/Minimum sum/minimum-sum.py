class Solution:
    def minSum(self, arr):
        # code here
        n=len(arr)
        dic={i:0 for i in range(10)}
        for i in range(n):
            dic[arr[i]]+=1
        even,odd,curr=[],[],True
        for i in range(10):
            cnt=dic[i]
            if cnt%2==0:
                even+=[i]*(cnt//2)
                odd+=[i]*(cnt//2)
            else:
                if curr:
                    even+=[i]*(cnt//2+1)
                    odd+=[i]*(cnt//2)
                else:
                    even+=[i]*(cnt//2)
                    odd+=[i]*(cnt//2+1)
                curr=not curr
        st=""
        carry=0
        i,j=len(even)-1,len(odd)-1
        while i>=0 or j>=0 or carry:
            sm=carry
            if i>=0:
                sm+=even[i]
            if j>=0:
                sm+=odd[j]
            if sm>9:
                st+=str(sm%10)
                carry=1
            else:
                st+=str(sm%10)
                carry=0
            i-=1
            j-=1
        return st[::-1].lstrip('0')
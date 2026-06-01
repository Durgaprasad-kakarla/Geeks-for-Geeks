class Solution:
    def findMaxProduct(self, arr):
        # code here
        prod=1
        mod=(10**9+7)
        maxi=-float('inf')
        neg_cnt,pos_cnt=0,0
        neg_prod=1
        for i in range(n):
            if arr[i]>0:
                prod=(prod*arr[i])
                pos_cnt+=1
            if arr[i]<0:
                neg_prod=(neg_prod*arr[i])
                maxi=max(maxi,arr[i])
                neg_cnt+=1
        if pos_cnt==0:
            if neg_cnt==0:
                return 0
            elif neg_cnt%2==0:
                return neg_prod%mod
            else:
                if neg_cnt==1:
                    return max(arr)
                return (neg_prod//maxi)%mod
        if neg_cnt%2==0:
            prod=(prod*neg_prod)
        else:
            prod=(prod*(neg_prod)//maxi)
        return prod%mod
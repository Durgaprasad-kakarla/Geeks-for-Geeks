class Solution:
    def minProd(self, arr):
        # code here
        n=len(arr)
        neg,pos,zero=0,0,0
        max_neg=-float('inf')
        pos_prod=1
        neg_prod=1
        for i in range(n):
            if arr[i]<0:
                max_neg=max(max_neg,arr[i])
                neg_prod*=arr[i]
                neg+=1
            elif arr[i]>0:
                pos_prod*=arr[i]
                pos+=1
            else:
                zero+=1
        if neg%2!=0:
            return pos_prod*neg_prod
        else:
            if neg==0:
                if zero==0:
                    return min(arr)
                return min(arr)
            # print(pos_prod,neg_prod,max_neg)
            return (pos_prod*neg_prod)//max_neg
            
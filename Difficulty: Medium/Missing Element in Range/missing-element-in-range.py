class Solution:
    def missingRange(self, arr, low, high):
        #code here
        n=len(arr)
        arr.sort()
        def lower_bound(arr,ele):
            n=len(arr)
            l,r=0,n-1
            while l<=r:
                mid=(l+r)//2
                if arr[mid]<ele:
                    l=mid+1
                else:
                    r=mid-1
            return r
        def upper_bound(arr,ele):
            n=len(arr)
            l,r=0,n-1
            while l<=r:
                mid=(l+r)//2
                if arr[mid]<=ele:
                    l=mid+1
                else:
                    r=mid-1
            return l
        lower,upper=lower_bound(arr,low),upper_bound(arr,high)
        # print(lower,upper)
        if lower==-1:
            lower=0
        if arr[lower]<low:
            lower+=1
        if upper==n:
            upper=n-1
        ind=lower
        missing=[]
        for i in range(low,high+1):
            while ind<n and  arr[ind]<i:
                ind+=1
            if ind<n and arr[ind]==i:
                ind+=1
            else:
                missing.append(i)
            # print(i,ind,missing)
        return missing
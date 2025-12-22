class Solution:
    def rowWithMax1s(self, arr):
        # code here
        def no_of_ones(arr):
            n=len(arr)
            l,r=0,n-1
            while l<=r:
                mid=(l+r)//2
                if arr[mid]<=1:
                    l=mid+1
                else:
                    r=mid-1
            upper_bound=l
            l,r=0,n-1
            while l<=r:
                mid=(l+r)//2
                if arr[mid]<1:
                    l=mid+1
                else:
                    r=mid-1
            lower_bound=l
            return (upper_bound-lower_bound)
        maxi=-float('inf')
        n=len(arr)
        for i in range(n):
            if maxi<no_of_ones(arr[i]):
               maxi=no_of_ones(arr[i])
               max_ind=i
        return -1 if maxi==-float('inf') else max_ind
            
            
class Solution:
    def countLessEqual(self, arr, x):
        #code here
        n=len(arr)
        if n==1:
            if arr[0]<=x:
                return 1
            return 0
        l,r=0,n-1
        rotated_ind=-1
        while l<=r:
            mid=(l+r)//2
            # print(l,r,mid)
            if mid==0:
                if mid+1<n and arr[mid]<arr[mid+1]:
                    rotated_ind=mid
                    break
            if mid==n-1:
                if mid-1>=0 and arr[mid]<arr[mid-1]:
                    rotated_ind=mid
                    break
            if mid-1>=0 and mid+1<n:
                if arr[mid-1]>arr[mid] and arr[mid]<arr[mid+1]:
                    rotated_ind=mid
                    break
            if arr[l]>arr[r]:
                if arr[l]<=arr[mid]:
                    l=mid+1
                else:
                    r=mid-1
            else:
                if arr[l]<=arr[mid]:
                    r=mid-1
                else:
                    l=mid+1
        def lower_bound(arr,l,r,ele):
            while l<=r:
                mid=(l+r)//2
                if arr[mid]<=ele:
                    l=mid+1
                else:
                    r=mid-1
            return l
        l1,r1,l2,r2=0,rotated_ind-1,rotated_ind,n-1
        # print(l1,r1,l2,r2)
        left=lower_bound(arr,l1,r1,x)
        right=lower_bound(arr,l2,r2,x)-l2
        # print(left,right)
        return left+right
            
                
        
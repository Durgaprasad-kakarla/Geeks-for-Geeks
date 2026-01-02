class Solution:
    def sort012(self, arr):
        # code here
        n=len(arr)
        l,mid,r=0,0,n-1
        while mid<=r:
            # print(l,mid,r)
            if arr[mid]==0:
                arr[l],arr[mid]=arr[mid],arr[l]
                l+=1
                mid+=1
            elif arr[mid]==1:
                mid+=1
            else:
                arr[r],arr[mid]=arr[mid],arr[r]
                r-=1
        return arr
        
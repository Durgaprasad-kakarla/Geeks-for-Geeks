class Solution:
    def aggressiveCows(self, arr, k):
        # code here
        n=len(arr)
        def position_crows(dist):
            cur=arr[0]
            tot_crows=1
            for i in range(1,n):
                if arr[i]-cur>=dist:
                    # print("in",arr[i],cur)
                    tot_crows+=1
                    cur=arr[i]
            return tot_crows
        arr.sort()
        l,r=0,arr[-1]-arr[0]
        while l<=r:
            mid=(l+r)//2
            # print(mid,position_crows(mid))
            if position_crows(mid)>=k:
                l=mid+1
            else:
                r=mid-1
        return r
        
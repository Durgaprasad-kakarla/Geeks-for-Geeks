class Solution:

    def aggressiveCows(self, stalls, k):
        # your code here
        def assign_stalls(arr,ele):
            n=len(arr)
            prev,cnt=arr[0],1
            for i in range(1,n):
                if arr[i]-prev>=ele:
                    cnt+=1
                    prev=arr[i]
            return cnt
        stalls.sort()
        l,r=0,max(stalls)-min(stalls)
        while l<=r:
            mid=(l+r)//2
            if assign_stalls(stalls,mid)>=k:
                l=mid+1
            else:
                r=mid-1
        return r

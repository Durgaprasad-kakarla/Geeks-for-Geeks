class Solution():
    def maxMinHeight(self, arr, k, w):
        # code here
        def func(arr,ele):
            n=len(arr)
            cnt,add=0,-1
            tot=0
            pref=[0]*(n+1)
            for i in range(n):
                if arr[i]<ele:
                    if i==0:
                        pref[i]+=(ele-arr[i])
                        pref[min(i+w,n)]-=(ele-arr[i])
                        tot+=(ele-arr[i])
                    else:
                        pref[i]+=pref[i-1]
                        sm=arr[i]+pref[i]
                        if sm<ele:
                            pref[i]+=(ele-sm)
                            pref[min(i+w,n)]-=(ele-sm)
                            tot+=(ele-sm)
                else:
                    pref[i]+=pref[i-1]
            # print(pref)
            return tot
        l,r=min(arr),sum(arr)+max(arr)
        while l<=r:
            mid=(l+r)//2
            # print(func(arr,mid),mid)
            if func(arr,mid)<=k:
                l=mid+1
            else:
                r=mid-1
        return r
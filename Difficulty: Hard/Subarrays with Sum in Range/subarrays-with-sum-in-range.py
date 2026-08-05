class Solution:
    def countSubarray(self, arr: list[int], l: int, r: int) -> int:
        # code here
        n=len(arr)
        pref=[0]*(n+1)
        for i in range(1,n+1):
            pref[i]+=pref[i-1]+arr[i-1]
        i=c=tot=ans=rem=0
        for s in range(n):
            while i<n and tot+arr[i]<=r:
                tot+=arr[i]
                i+=1
            while c<n and pref[c+1]-rem<l:
                c+=1
            tot-=arr[s]
            rem+=arr[s]
            ans+=(i-c)
        return ans
        
class Solution:
    def kBitFlips(self, arr, k):
        # code here
        n=len(arr)
        pref=[0]*(n+2)
        cnt=0
        for i in range(1,n+1):
            pref[i]+=pref[i-1]
            if pref[i]%2==0:
                if arr[i-1]==0:
                    pref[i]+=1
                    if i+k>n+1:
                        return -1
                    pref[i+k]-=1
                    cnt+=1
            else:
                if arr[i-1]==1:
                    pref[i]+=1
                    if i+k>n+1:
                        return -1
                    pref[i+k]-=1
                    cnt+=1
                    
        return cnt
        
class Solution:
    def countPairs(self, arr: list[int], k: int) -> int:
        # code here
        l,r=0,0
        arr.sort()
        n=len(arr)
        tot=0
        while r<n:
            # print(l,r)
            if arr[r]-arr[l]<k:
                r+=1
            else:
                # print('in',l,r)
                tot+=(r-l-1)
                l+=1
        cur=(r-l-1)
        return tot+(cur*(cur+1))//2
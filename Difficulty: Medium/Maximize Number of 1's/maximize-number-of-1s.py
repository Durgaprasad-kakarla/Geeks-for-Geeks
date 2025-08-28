class Solution:
    def maxOnes(self, arr, k):
        # code here
        n=len(arr)
        start,cnt_0,max_len=0,0,0
        for i in range(n):
            if arr[i]==0:
                cnt_0+=1
            while start<n and cnt_0>k:
                if arr[start]==0:
                    cnt_0-=1
                start+=1
            max_len=max(max_len,i-start+1)
        return max_len
            
        
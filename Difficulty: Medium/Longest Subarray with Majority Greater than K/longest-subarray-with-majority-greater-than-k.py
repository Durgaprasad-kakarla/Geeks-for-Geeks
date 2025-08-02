class Solution:
    def longestSubarray(self, arr, k):
        # Code Here 
        n=len(arr)
        dic={0:-1}
        pref,maxi=0,0
        for i in range(n):
            if arr[i]>k:
                pref+=1
            else:
                pref-=1
            if pref>0:
                maxi=max(maxi,i+1)
            else:
                if pref-1 in dic:
                    maxi=max(maxi,(i-dic[pref-1]))
            if pref not in dic:
                dic[pref]=i
        return maxi
            
            
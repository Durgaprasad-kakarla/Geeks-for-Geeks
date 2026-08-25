from bisect import bisect_left
class Solution:
    def minMoves(self, arr):
        """code here"""
        n=len(arr)
        dic={}
        for i in range(n):
            dic[arr[i]]=i
        vis=set()
        maxi=0
        for i in range(1,n+1):
            ind=dic[i]
            if i not in vis:
                vis.add(i)
                cur=i+1
                cnt=1
                while cur in dic and dic[cur]>ind:
                    vis.add(cur)
                    ind=dic[cur]
                    cur+=1
                    cnt+=1
                # print(vis)
                maxi=max(maxi,cnt)
        return n-maxi
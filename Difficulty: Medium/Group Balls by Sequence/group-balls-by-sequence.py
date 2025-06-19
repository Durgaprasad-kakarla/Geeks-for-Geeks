import heapq
class Solution:
    def validgroup(self, arr ,k):
        # Code here
        st=set(arr)
        n=len(arr)
        for i in range(n):
            if arr[i]-1 not in st:
                curr,cnt=arr[i],1
                while curr+1 in st:
                    curr+=1
                    cnt+=1
                if cnt%k!=0:
                    return False
        return True
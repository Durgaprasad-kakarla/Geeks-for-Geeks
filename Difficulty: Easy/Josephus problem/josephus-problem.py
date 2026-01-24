class Solution:
    def josephus(self, n, k):
        # code here
        arr=[i+1 for i in range(n)]
        def eliminate(arr,start,k):
            i=start
            while i<n and k>=0:
                if arr[i]!=-1:
                    k-=1
                    if k==0:
                        return i
                i=(i+1)%n
            return i
        curr=0
        i=0
        while i+1<n:
            ind=eliminate(arr,curr,k)
            arr[ind]=-1
            curr=ind
            # print(arr)
            i+=1
        for i in range(n):
            if arr[i]!=-1:
                return arr[i]
        return -1
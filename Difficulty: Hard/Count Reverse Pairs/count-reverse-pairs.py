class Solution:
    def countRevPairs(self, arr):
        # Code here
        def merge(l,mid,r):
            low,high=l,mid+1
            lst=[]
            cnt=0
            i,j=low,high
            while i<=mid:
                while j<=r and arr[i]>2*arr[j]:
                    j+=1
                cnt+=(j-(mid+1))
                i+=1
            while low<=mid and high<=r:
                if arr[low]<=arr[high]:
                    lst.append(arr[low])
                    low+=1
                else:
                    lst.append(arr[high])
                    high+=1
            while low<=mid:
                lst.append(arr[low])
                low+=1
            while high<=r:
                lst.append(arr[high])
                high+=1
            for i in range(l,r+1):
                arr[i]=lst[i-l]
            return cnt
        def mergesort(l,r):
            if l>=r:
                return 0
            mid=(l+r)//2
            cnt=mergesort(l,mid)
            cnt+=mergesort(mid+1,r)
            cnt+=merge(l,mid,r)
            return cnt
        n=len(arr)
        cnt=mergesort(0,n-1)
        return cnt
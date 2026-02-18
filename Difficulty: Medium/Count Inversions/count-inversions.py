class Solution:
    def inversionCount(self, arr):
        # Code Here
        def merge(l,mid,r):
            low,high=l,mid+1
            cnt=0
            while low<=mid:
                while high<=r and arr[low]>arr[high]:
                    high+=1
                cnt+=(high-(mid+1))
                low+=1
            low,high=l,mid+1
            lst=[]
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
        return mergesort(0,len(arr)-1)
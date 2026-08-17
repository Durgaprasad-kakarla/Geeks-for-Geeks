class Solution:
    def inversionCount(self, arr):
        # code here
        n=len(arr)
        def merge_sort(l,r):
            if l>=r:
                return 0
            mid=(l+r)//2
            cnt=0
            cnt+=merge_sort(l,mid)
            cnt+=merge_sort(mid+1,r)
            cnt+=merge(l,mid,r)
            return cnt
        def merge(l,mid,r):
            low,high=l,mid+1
            tot=0
            j=mid+1
            lst=[]
            while low<=mid:
                while j<=r and arr[low]>arr[j]:
                    j+=1
                low+=1
                tot+=(j-(mid+1))
            # print(tot)
            low,high=l,mid+1
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
            return tot
        return merge_sort(0,n-1)
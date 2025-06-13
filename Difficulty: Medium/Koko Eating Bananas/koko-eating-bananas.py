#User function Template for python3
import math
class Solution:
    def kokoEat(self,arr,k):
        # Code here
        def hours_taken_to_eat(arr,ele):
            days=0
            for i in arr:
                days+=math.ceil(i/ele)
            return days
        l,r=1,max(arr)
        while l<=r:
            mid=(l+r)//2
            if hours_taken_to_eat(arr,mid)<=k:
                r=mid-1
            else:
                l=mid+1
        return l
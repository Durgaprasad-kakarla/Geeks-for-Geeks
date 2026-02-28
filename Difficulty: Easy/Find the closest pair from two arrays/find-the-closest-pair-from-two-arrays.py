class Solution:
    def findClosestPair(self,arr1, arr2, x):
        #code here
        def get_closest(arr1,arr2):
            n,m=len(arr1),len(arr2)
            l,r=0,m-1
            mini=float('inf')
            pair=[]
            while l<n and r>=0:
                if mini>abs(x-(arr1[l]+arr2[r])):
                    mini=abs(x-(arr1[l]+arr2[r]))
                    pair=[arr1[l],arr2[r]]
                if arr1[l]+arr2[r]<=x:
                    l+=1
                else:
                    r-=1
            return mini,pair
        min1,pair1=get_closest(arr1,arr2)
        min2,pair2=get_closest(arr2,arr1)
        if min1<min2:
            return pair1
        return pair2
        
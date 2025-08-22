from bisect import bisect_left
class Solution:
    def median(self, mat):
    	# code here 
        n,m=len(mat),len(mat[0])
        k=(n*m)//2+1
        mini,maxi=float('inf'),-float('inf')
        for lst in mat:
            mini=min(mini,min(lst))
            maxi=max(maxi,max(lst))
        def count_elements(ele):
            n,m=len(mat),len(mat[0])
            cnt,maxi=0,0
            for i in range(n):
                ind=bisect_left(mat[i],ele)
                if ind>0:
                    maxi=max(maxi,mat[i][ind-1])
                cnt+=(ind)
            return cnt,maxi
        l,r=mini,maxi
        ans=maxi
        while l<=r:
            mid=(l+r)//2
            cnt,maxi=count_elements(mid)
            if cnt>=k:
                ans=maxi
                r=mid-1
            else:
                l=mid+1
        return ans
        
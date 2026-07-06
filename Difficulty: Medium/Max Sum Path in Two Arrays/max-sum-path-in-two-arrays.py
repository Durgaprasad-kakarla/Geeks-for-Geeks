import bisect
class Solution:
    def maxPathSum(self, a, b):
        # Code here
        n,m=len(a),len(b)
        common=[]
        for i in range(n):
            ind=bisect.bisect_left(b,a[i])
            if ind<m and b[ind]==a[i]:
                common.append([i,ind])
        pref_a,pref_b=[0]*(n+1),[0]*(m+1)
        for i in range(1,n+1):
            pref_a[i]+=pref_a[i-1]+a[i-1]
        for i in range(1,m+1):
            pref_b[i]+=pref_b[i-1]+b[i-1]
        last_a,last_b=0,0
        sm=0
        for i,j in common:
            maxi=max(pref_a[i+1]-pref_a[last_a],pref_b[j+1]-pref_b[last_b])
            # print(pref_a[i+1],pref_a[last_a],pref_b[j+1],pref_b[last_b])
            last_a,last_b=i+1,j+1
            sm+=maxi
        # print(pref_a)
        # print(pref_b)
        # print(sm,last_a,last_b,pref_a[n]-pref_a[last_a])
        return sm+max(pref_a[n]-pref_a[last_a],pref_b[m]-pref_b[last_b])
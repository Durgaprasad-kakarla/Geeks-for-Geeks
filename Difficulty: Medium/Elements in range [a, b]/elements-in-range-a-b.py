class Fenwick:
    def __init__(self,n):
        self.fenwick=[0]*(n+1)
        self.n=n
    def update(self,ind,ele):
        while ind<=self.n:
            self.fenwick[ind]+=ele
            ind+=(ind & (-ind))
    def sum_range(self,ind):
        sm=0
        while ind>0:
            sm+=self.fenwick[ind]
            ind-=(ind & (-ind))
        return sm


class Solution:
    def cntInRange(self, arr, queries):
        # code here
        n=len(arr)
        max_ele=max(arr)
        pref=[0]*(max_ele+1)
        for i in range(n):
            pref[arr[i]]+=1
        for i in range(1,max_ele+1):
            pref[i]+=pref[i-1]
        res=[]
        for l,r in queries:
            if l>max_ele:
                res.append(0)
            elif r<0:
                res.append(0)
            else:
                if l-1<0:
                    left=0
                else:
                    left=pref[l-1]
                if r>max_ele:
                    right=pref[max_ele]
                else:
                    right=pref[r]
                res.append(right-left)
        return res
import math
class SegmentTree:
    def __init__(self,n):
        self.n=4*n
        self.seg=[0 for _ in range(4*n)]
    def lcm(self,ele1,ele2):
        return (ele1*ele2)//math.gcd(ele1,ele2)
    def build(self,ind,l,r,arr):
        if l==r:
            self.seg[ind]=arr[l]
            return self.seg[ind]
        mid=(l+r)//2
        left=self.build(2*ind+1,l,mid,arr)
        right=self.build(2*ind+2,mid+1,r,arr)
        self.seg[ind]=self.lcm(left,right)
        return self.seg[ind]
    def range(self,ind,low,high,l,r):
        if low<=l and r<=high:
            return self.seg[ind]
        if r<low or l>high:
            return 1
        mid=(l+r)//2
        left=self.range(2*ind+1,low,high,l,mid)
        right=self.range(2*ind+2,low,high,mid+1,r)
        return self.lcm(left,right)
    def update(self,ind,l,r,index,val,arr):
        if l==r:
            self.seg[ind]=val
            arr[index]=val
            return
        mid=(l+r)//2
        if index<=mid:
            self.update(2*ind+1,l,mid,index,val,arr)
        else:
            self.update(2*ind+2,mid+1,r,index,val,arr)
        
        self.seg[ind]=self.lcm(self.seg[2*ind+1],self.seg[2*ind+2])
class Solution:
    def RangeLCMQuery(self, arr, queries):
        # code here
        n=len(arr)
        s=SegmentTree(n)
        s.build(0,0,n-1,arr)
        ans=[]
        for typ,x,y in queries:
            if typ==1:
                s.update(0,0,n-1,x,y,arr)
            else:
                lcm=s.range(0,x,y,0,n-1)
                ans.append(lcm)
        return ans
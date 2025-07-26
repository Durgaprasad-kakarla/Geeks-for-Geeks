class Solution:
    def findMajority(self, arr):
        # code here
        n=len(arr)
        cnt1,cnt2,ele1,ele2=0,0,-1,-1
        for i in range(n):
            if cnt1==0 and ele2!=arr[i]:
                ele1=arr[i]
                cnt1+=1
            elif ele1==arr[i]:
                cnt1+=1
            elif ele2==arr[i]:
                cnt2+=1
            elif cnt2==0:
                ele2=arr[i]
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
        cnt1,cnt2=0,0
        for i in range(n):
            if ele1==arr[i]:
                cnt1+=1
            if ele2==arr[i]:
                cnt2+=1
        lst=[]
        if cnt1>n//3:
            lst.append(ele1)
        if cnt2>n//3:
            lst.append(ele2)
        return sorted(lst)
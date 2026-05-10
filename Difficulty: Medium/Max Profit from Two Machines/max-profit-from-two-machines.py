class Solution:
    def maxProfit(self, x, y, a, b):
        # code here
        crr=[]
        for i in range(n):
            if arr[i]>brr[i]:
                crr.append([arr[i]-brr[i],0,i])
            elif arr[i]==brr[i]:
                crr.append([0,0,i])
            else:
                crr.append([brr[i]-arr[i],1,i])
        crr.sort(reverse=True)
        tot=0
        for i in range(n):
            diff,l,ind=crr[i]
            if l==0:
                x-=1
                if x>=0:
                    tot+=(arr[ind])
                else:
                    tot+=(brr[ind])
            else:
                y-=1
                if y>=0:
                    tot+=(brr[ind])
                else:
                    tot+=(arr[ind])
        return tot

class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        #code here
        wt_val=[]
        n=len(wt)
        for i in range(n):
            wt_val.append([wt[i]/val[i],wt[i],val[i]])
        wt_val.sort()
        tot=0
        for i in range(n):
            if capacity>=wt_val[i][1]:
                tot+=wt_val[i][2]
                capacity-=wt_val[i][1]
            else:
                tot+=(capacity/wt_val[i][1])*wt_val[i][2]
                break
        return tot
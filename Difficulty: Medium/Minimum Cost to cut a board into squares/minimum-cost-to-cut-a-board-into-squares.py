class Solution:
    def minCost(self, n, m, x, y):
        # code here
        x.sort(reverse=True)
        y.sort(reverse=True)
        m,n=len(x),len(y)
        i,j,tot=0,0,0
        vertical,horizontal=1,1
        while i<m and j<n:
            if x[i]>y[j]:
                tot+=x[i]*horizontal
                # print("hor",x[i]*horizontal)
                i+=1
                vertical+=1
            else:
                tot+=y[j]*vertical
                # print("ver",y[j]*vertical)
                j+=1
                horizontal+=1
        while i<m:
            tot+=x[i]*horizontal
            i+=1
            vertical+=1
        while j<n:
            tot+=y[j]*vertical
            j+=1
            horizontal+=1
        return tot
        
        
        

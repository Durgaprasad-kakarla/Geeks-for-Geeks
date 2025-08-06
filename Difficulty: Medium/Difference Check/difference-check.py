class Solution:
    def minDifference(self, arr):
        # code here
        tot_seconds=[]
        n=len(arr)
        for i in range(n):
            h,m,s=arr[i].split(":")
            tot_seconds.append(int(h)*3600+int(m)*60+int(s))
        tot_seconds.sort()
        mini=(24*3600-tot_seconds[-1]+tot_seconds[0])
        for i in range(1,n):
            mini=min(mini,tot_seconds[i]-tot_seconds[i-1])
        return mini
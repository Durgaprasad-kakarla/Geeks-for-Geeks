#User function Template for python3

class Solution:
    def pairAndSum(self, n, arr):
        #code here
        sm=0
        lst=[0]*32
        for i in range(n):
            for j in range(32):
                if (1<<j)&arr[i]:
                    lst[j]+=1
        for i in range(len(lst)):
            x=lst[i]-1
            if x>0:
                sm+=(x*(x+1))//2*(2**i)
        return sm
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Arr=list(map(int,input().strip().split(' ')))
        ob=Solution()
        print(ob.pairAndSum(N,Arr))
# } Driver Code Ends
class Solution:
    def findSwapValues(self,a, n, b, m):
        # Your code goes here
        sm1=sum(a)
        sm2=sum(b)
        diff=abs(sm1-sm2)
        if diff&1==1:
            return -1
        else:
            a.sort()
            b.sort()
            l,r=0,0
            while l<n and r<m:
                if a[l]<b[r]:
                    if b[r]-a[l]==diff//2:
                        return 1
                    elif b[r]-a[l]>diff//2:
                        l+=1
                    else:
                        r+=1
                else:
                    if a[l]-b[r]==diff//2:
                        return 1
                    elif a[l]-b[r]>diff//2:
                        r+=1
                    else:
                        l+=1
            return -1


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        m=l[1]
        a = list(map(int,input().split()))
        b = list(map(int, input().split()))
        ob = Solution()
        print(ob.findSwapValues(a,n,b,m))
# } Driver Code Ends
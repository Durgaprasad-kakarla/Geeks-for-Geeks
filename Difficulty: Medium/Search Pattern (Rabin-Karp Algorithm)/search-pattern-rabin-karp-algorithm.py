#User function Template for python3

class Solution:
    def search(self, pattern, txt):
        # code here
        q=(10**9+7)
        n,m,h,d=len(txt),len(pattern),1,5
        for i in range(1,m):
            h=(h*d)%q
        t,p=0,0
        for i in range(m):
            t=(t*d+(ord(txt[i])))%q
            p=(p*d+(ord(pattern[i])))%q
        lst=[]
        for i in range(n-m+1):
            if t==p:
                flag=0
                for j in range(m):
                    if txt[i+j]!=pattern[j]:
                        flag=1
                        break
                if flag==0:
                    lst.append(i+1)
            if i<n-m:
                t=(d*(t-(ord(txt[i]))*h)+(ord(txt[i+m])))%q
                if t<0:
                    t+=q
        return lst
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        for value in ans:
            print(value,end = ' ')
        print()
# } Driver Code Ends
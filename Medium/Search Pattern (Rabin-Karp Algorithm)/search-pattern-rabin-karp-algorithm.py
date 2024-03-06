#User function Template for python3

class Solution:
    def search(self, pattern, text):
        # code here
        q,d=101,10
        m=len(pattern)
        n=len(text)
        i,j,h=0,0,1
        for i in range(m-1):
            h=(h*d)%q
        p,t=0,0
        for i in range(m):
            p=(p*d+ord(pattern[i]))%q
            t=(t*d+ord(text[i]))%q
        lst=[]
        for i in range(n-m+1):
            if p==t:
                for j in range(m):
                    if text[i+j]!=pattern[j]:
                        break
                j+=1
                if j==m:
                    lst.append(i+1)
            if i<n-m:
                t=(d*(t-ord(text[i])*h)+ord(text[i+m]))%q
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
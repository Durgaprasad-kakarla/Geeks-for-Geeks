#User function Template for python3

class Solution:
    def recamanSequence(self, n):
        # code here
        # if n==1:
        #     return [0]
        a=0
        lst=[]
        lst.append(0)
        dic={}
        dic[0]=1
        x=1
        while x<=n:
            if a-x<=0 or (a-x) in dic:
                lst.append(a+x)
                dic[a+x]=1
                a=a+x
            else:
                lst.append(a-x)
                dic[a-x]=1
                a=a-x
            x+=1
        return lst


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.recamanSequence(n)
        for i in range(n):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends
class Solution:
    def countAndSay(self, n):
        # code here
        st='1'
        for _ in range(1,n):
            k=len(st)
            new_st,cnt="",1
            for i in range(1,k):
                if st[i-1]==st[i]:
                    cnt+=1
                else:
                    new_st+=(str(cnt)+st[i-1])
                    cnt=1
            if cnt>0:
                new_st+=(str(cnt)+st[k-1])
            st=new_st
        return st
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.countAndSay(n))

        print("~")
# } Driver Code Ends
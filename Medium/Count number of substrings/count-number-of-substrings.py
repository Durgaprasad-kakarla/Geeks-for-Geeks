
class Solution:
    def substrCount (self,s, k):
        # your code here
        def substrings_with_atleastk(s,k):
            n=len(s)
            j,f,cnt=0,0,0
            dic={}
            for i in range(n):
                while j<n and f<k:
                    if s[j] not in dic or dic[s[j]]==0:
                        dic[s[j]]=1
                        f+=1
                    else:
                        dic[s[j]]+=1
                    j+=1
                if f==k:
                    cnt+=(n-j+1)
                dic[s[i]]-=1
                if dic[s[i]]==0:
                    f-=1
            return cnt
        return (substrings_with_atleastk(s,k)-substrings_with_atleastk(s,k+1))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    k = int (input ())
    ob = Solution()
    print (ob.substrCount (s, k))
# } Driver Code Ends
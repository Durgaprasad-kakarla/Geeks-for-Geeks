#User function Template for python3

class Solution:

    def longestKSubstr(self, s, k):
        # code here
        maxi,n,start,f=-float('inf'),len(s),0,0
        dic={}
        for i in range(n):
            while start<n and f==k and (s[i] not in dic or dic[s[i]]==0):
                dic[s[start]]-=1
                if dic[s[start]]==0:
                    f-=1
                start+=1
            if s[i] in dic and dic[s[i]]>0:
                dic[s[i]]+=1
            else:
                dic[s[i]]=1
                f+=1
            if f==k:
                maxi=max(maxi,i-start+1)
        return maxi if maxi!=-float('inf') else -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

        print("~")
# } Driver Code Ends
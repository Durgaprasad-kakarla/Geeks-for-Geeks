#User function Template for python3

class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        n=len(s)
        dic,start,maxi={},0,0
        for i in range(n):
            if s[i] in dic and dic[s[i]]>0:
                while start<n and s[start]!=s[i]:
                    dic[s[start]]-=1
                    start+=1
                dic[s[start]]-=1
                start+=1
            maxi=max(maxi,i-start+1)
            dic[s[i]]=1
        return maxi
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.longestUniqueSubstr(s)

        print(ans)

        print("~")
# } Driver Code Ends
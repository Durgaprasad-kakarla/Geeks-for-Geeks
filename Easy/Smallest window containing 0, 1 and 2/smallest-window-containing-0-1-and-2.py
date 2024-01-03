#User function Template for python3

class Solution:
    def smallestSubstring(self, S):
        # Code here
        n=len(S)
        j,p=0,3
        f=0
        dic={}
        mini=float('inf')
        for i in range(n):
            while j<n and f<p:
                if S[j] not in dic or dic[S[j]]==0:
                    f+=1
                    dic[S[j]]=1
                else:
                    dic[S[j]]+=1
                j+=1
            if f==p:
                mini=min(mini,j-i)
            dic[S[i]]-=1
            if dic[S[i]]==0:
                f-=1
        return mini if mini!=float('inf') else -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S = input()
		ob = Solution()
		ans = ob.smallestSubstring(S)
		
		print(ans)



# } Driver Code Ends
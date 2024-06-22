class Solution:
    def ExtractNumber(self,sentence):
        #code here
        n=len(sentence)
        maxi=-1
        x=-1
        flag=0
        for i in range(n):
            if sentence[i].isnumeric():
                if sentence[i]=='9':
                    flag=1
                if x==-1:
                    x=i
            else:
                if flag!=1 and x!=-1:
                    maxi=max(maxi,int(sentence[x:i]))
                x=-1
                flag=0
        return maxi
                


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    S = input()
    ob = Solution()
    ans = ob.ExtractNumber(S)
    print(ans)

# } Driver Code Ends
class Solution:
    def minChar(self, s):
        #Write your code here
        def LPS_of_string(s):
            n=len(s)
            lps=[0]*n
            i,length=1,0
            while i<n:
                if s[i]==s[length]:
                    lps[i]=length+1
                    length+=1
                    i+=1
                else:
                    if length!=0:
                        length=lps[length-1]
                    else:
                        lps[i]=0
                        i+=1
            return lps
        return len(s)-(LPS_of_string(s+s[::-1]))[-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        obj = Solution()
        ans = obj.minChar(s)
        print(ans)
        print("~")

# } Driver Code Ends
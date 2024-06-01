
class Solution:
    def oddEven(self, s : str) -> str:
        # code here
        alphabets_count=[0]*26
        n=len(s)
        for i in range(n):
            alphabets_count[ord(s[i])-97]+=1
        tot=0
        for i in range(26):
            if alphabets_count[i]>0:
                if (i+1)&1 and alphabets_count[i]&1:
                    tot+=1
                elif (i+1)&1==0 and alphabets_count[i]&1==0:
                    tot+=1 
        if tot&1==1:
            return 'ODD'
        else:
            return 'EVEN'
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s = (input())

        obj = Solution()
        res = obj.oddEven(s)

        print(res)

# } Driver Code Ends
#User function Template for python3
import heapq
class Solution:
    
    #Function to find the largest number after k swaps.
    def findMaximumNum(self, s, k):
        #code here
        n=len(s)
        global ans
        def func(ind,k,s):
            global ans
            if k==0 or ind==len(s):
                f="".join(s.copy())
                ans=max(f,ans)
                return 
            for i in range(ind,n):
                if s[i]>s[ind]:
                    s[i],s[ind]=s[ind],s[i]
                    func(ind+1,k-1,s)
                    s[i],s[ind]=s[ind],s[i]
            func(ind+1,k,s)
        ans=""
        s=list(s)
        func(0,k,s)
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        k = int(input())
        s = input()
        ob = Solution()
        print(ob.findMaximumNum(s, k))

        print("~")

# } Driver Code Ends
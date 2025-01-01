#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def sieve(self):
        pass
    def findPrimeFactors(self, n):
        # Code here
        i=2
        ans=[]
        while i*i<=n:
            if n%i==0:
                while n%i==0:
                    ans.append(i)
                    n//=i
            i+=1
        if n>=2:
            ans.append(n)
        return ans
                

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    ob = Solution()
    ob.sieve()
    for _ in range (t):
        n = int(input())
        ans = ob.findPrimeFactors(n)
        for v in ans:
            print(v, end = ' ')
        print()
        print("~")
# } Driver Code Ends
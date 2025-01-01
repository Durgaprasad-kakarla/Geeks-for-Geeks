#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def print_divisors(self, n):
        # code here
        if n==1:
            print(1,end=" ")
        else:
            ans=[1,n]
            i=2
            while i*i<=n:
                if n%i==0:
                    ans.append(i)
                    if i!=n//i:
                        ans.append(n//i)
                i+=1
            ans.sort()
            for i in ans:
                print(i,end=" ")

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        ob.print_divisors(N)
        print()
        print("~")
# } Driver Code Ends
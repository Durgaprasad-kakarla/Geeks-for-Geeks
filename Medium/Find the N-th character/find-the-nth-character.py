#User function Template for python3

class Solution:
    def nthCharacter(self, s, r, n):
        # code here
        rem=n%(2**r)
        d=n//(2**r)
        ele=s[d]
        for i in range(r):
            ele = ele.translate(str.maketrans({'0': '01', '1': '10'}))
        return ele[rem]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        snr = input().split()
        S, R, N = snr[0], int(snr[1]), int(snr[2])
        ob = Solution()
        print(ob.nthCharacter(S, R, N))
# } Driver Code Ends
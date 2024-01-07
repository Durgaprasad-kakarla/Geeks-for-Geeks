#User function Template for python3

class Solution:
    def splitArray(self, nums, n,k):
        # code here 
        l,r = max(nums), sum(nums)
        while l < r:
            mid = (l+r)//2
            tot, cnt = 0, 1
            for num in nums:
                if tot+num<=mid: 
                    tot += num
                else:
                    tot = num
                    cnt += 1
            if cnt>k:
                 l= mid+1
            else:  
                r= mid
        return r

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.splitArray(arr,N,K))
# } Driver Code Ends
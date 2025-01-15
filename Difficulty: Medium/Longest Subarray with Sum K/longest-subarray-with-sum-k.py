# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        n=len(arr)
        maxi,dic,pref=0,{0:-1},0
        for i in range(n):
            pref+=arr[i]
            if pref-k in dic:
                maxi=max(maxi,i-dic[pref-k])
            if pref not in dic:
                dic[pref]=i
        return maxi
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends
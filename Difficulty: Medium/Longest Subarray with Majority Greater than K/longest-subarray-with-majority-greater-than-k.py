#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
class Solution:
    def longestSubarray(self, arr, k):
        # Code Here
        n=len(arr)
        maxi,pref=0,0
        dic={0:-1}
        for i in range(n):
            if arr[i]>k:
                pref+=1
            else:
                pref-=1
            if pref>0:
                maxi=max(maxi,i+1)
            else:
                if pref-1 in dic:
                    maxi=max(maxi,i-dic[pref-1])
            if pref not in dic:
                dic[pref]=i
        return maxi


#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        
        arr = [int(x) for x in input().strip().split()]
        k = int(input())
        
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        print("~")
        t -= 1
# } Driver Code Ends
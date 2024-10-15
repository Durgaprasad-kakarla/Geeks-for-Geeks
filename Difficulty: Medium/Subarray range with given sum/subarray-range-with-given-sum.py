#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Complete this fuction
    #Function to count the number of subarrays which adds to the given sum.
    def subArraySum(self,arr, tar):
        #Your code here
        dic={0:1}
        pref,n,count=0,len(arr),0
        for i in range(n):
            pref+=arr[i]
            if pref-tar in dic:
                count+=dic[pref-tar]
            if pref in dic:
                dic[pref]+=1
            else:
                dic[pref]=1
        return count

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        tar= int(input())
        ob = Solution()
        res = ob.subArraySum(arr,tar)
        print(res)
        # print("~")
        t -= 1


# } Driver Code Ends
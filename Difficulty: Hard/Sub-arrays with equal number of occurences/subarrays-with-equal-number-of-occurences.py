#User function Template for python3

class Solution:
    def sameOccurrence(self, arr, x, y):
        # code here
        n=len(arr)
        for i in range(n):
            if arr[i]==x:
                arr[i]=1
            elif arr[i]==y:
                arr[i]=-1
            else:
                arr[i]=0
        dic={0:1}
        ans,pref=0,0
        for i in range(n):
            pref+=arr[i]
            if pref in dic:
                ans+=dic[pref]
            if pref in dic:
                dic[pref]+=1
            else:
                dic[pref]=1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        x = int(input().strip())
        y = int(input().strip())
        ob = Solution()
        ans = ob.sameOccurrence(arr, x, y)
        print(ans)
        tc -= 1

# } Driver Code Ends
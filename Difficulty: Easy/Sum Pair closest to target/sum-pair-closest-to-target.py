#User function Template for python3
class Solution:
    def sumClosest(self, arr, target):
        # code here
        arr.sort()
        n=len(arr)
        l,r=0,n-1
        mini=float('inf')
        maxi=-float('inf')
        pair=[]
        while l<r:
            # print(l,r)
            if mini>abs(target-(arr[l]+arr[r])):
                mini=abs(target-(arr[l]+arr[r]))
                maxi=r-l
                pair=[arr[l],arr[r]]
            elif mini==abs(target-(arr[l]+arr[r])):
                if maxi<(r-l):
                    maxi=r-l
                    pair=[arr[l],arr[r]]
            if arr[l]+arr[r]<target:
                l+=1
            else:
                r-=1
        return pair


# 5 10 20 30
# 0 1  2   3

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    while t > 0:
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        ans = ob.sumClosest(arr, target)
        if not ans:
            print("[]")
        else:
            print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends
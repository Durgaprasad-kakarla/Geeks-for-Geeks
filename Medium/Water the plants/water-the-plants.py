#User function Template for python3

class Solution:
    def min_sprinklers(self, gallery, n):
        # code here
        arr=[]
        for i in range(n):
            arr.append([i-gallery[i],i+gallery[i]])
        arr.sort()
        target=0
        ans,i=0,0
        while target<n:
            if i==len(arr) or arr[i][0]>target:
                return -1
            max_range=arr[i][1]
            while i+1<n and arr[i+1][0]<=target:
                i+=1
                max_range=max(max_range,arr[i][1])
            if max_range<target:
                return -1
            ans+=1
            target=max_range+1
            i+=1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        gallery = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.min_sprinklers(gallery,n))

# } Driver Code Ends
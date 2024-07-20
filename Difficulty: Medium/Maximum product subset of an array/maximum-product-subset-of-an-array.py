#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def findMaxProduct(self, arr):
        # Write your code here
        n=len(arr)
        tot,cnt,cnt_0=1,0,0
        maxi=-float('inf')
        pos=0
        for i in range(n):
            if arr[i]<0:
                maxi=max(maxi,arr[i])
                tot*=arr[i]
                cnt+=1
            elif arr[i]==0:
                cnt_0+=1
            else:
                pos+=1
                tot*=arr[i]
        if cnt%2==0:
            if tot==1 and pos==0 and (cnt>0 and cnt%2!=0):
                return 0
            return tot%(10**9+7)
        else:
            # print(cnt,tot,pos)
            # print(tot//maxi)
            if tot==-1 and pos==0 and (cnt>0 and cnt%2!=0):
                return 0
            return (tot//maxi)%(10**9+7)
        
        
    


#{ 
 # Driver Code Starts.
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        solution = Solution()
        ans = solution.findMaxProduct(arr)
        results.append(ans)
    
    for result in results:
        print(result)
# } Driver Code Ends
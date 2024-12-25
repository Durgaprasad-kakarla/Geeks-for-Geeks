#User function Template for python3
class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, val, wt, capacity):
        #code here
        n=len(val)
        arr=[]
        for i in range(n):
            arr.append([wt[i]/val[i],wt[i],val[i]])
        arr.sort()
        tot=0
        for i in range(n):
            _,wt,val=arr[i][0],arr[i][1],arr[i][2]
            if wt<=capacity:
                tot+=val
                capacity-=wt
            else:
                tot+=(val/wt)*(capacity)
                capacity=0
        return tot


#{ 
 # Driver Code Starts
#Position this line where user code will be pasted.

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        # Read values array
        values = list(map(int, input().strip().split()))

        # Read weights array
        weights = list(map(int, input().strip().split()))

        # Read the knapsack capacity
        W = int(input().strip())

        ob = Solution()
        print("%.6f" % ob.fractionalknapsack(values, weights, W))
        print("~")

# } Driver Code Ends
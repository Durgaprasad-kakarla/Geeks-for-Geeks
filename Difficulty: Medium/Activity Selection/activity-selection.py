class Solution:
    def activitySelection(self, start, finish):
        #code here
        arr=[]
        n=len(start)
        for i in range(n):
            arr.append([start[i],finish[i]])
        arr.sort(key=lambda x:x[1])
        cnt,end=1,arr[0][1]
        for i in range(1,n):
            if end<arr[i][0]:
                end=arr[i][1]
                cnt+=1
        return cnt

#{ 
 # Driver Code Starts
def main():
    t = int(input().strip())  # Number of test cases

    for _ in range(t):
        # Read the start times
        start = list(map(int, input().strip().split()))

        # Read the finish times
        finish = list(map(int, input().strip().split()))

        # Create solution object and call activitySelection
        obj = Solution()
        print(obj.activitySelection(start, finish))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
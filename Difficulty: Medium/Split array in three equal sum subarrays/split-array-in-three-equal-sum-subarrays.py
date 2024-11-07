#User function Template for python3
class Solution:
    # Function to determine if array arr can be split into three equal sum sets.
    def findSplit(self, arr):
        #cod here
        n=len(arr)
        length=sum(arr)//3
        if sum(arr)%3!=0:
            return [-1,-1]
        if sum(arr)==0:
            return [1,2]
        index=[]
        sm=0
        for i in range(n):
            sm+=arr[i]
            if sm==length:
                if len(index)==0:
                    index.append(i)
            elif sm==length*2:
                if len(index)==1:
                    index.append(i)
                    return index
        return [-1,-1]


#{ 
 # Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.findSplit(arr)

        if result == [-1, -1]:
            print("false")
        else:
            print("true")
        print("~")

# } Driver Code Ends
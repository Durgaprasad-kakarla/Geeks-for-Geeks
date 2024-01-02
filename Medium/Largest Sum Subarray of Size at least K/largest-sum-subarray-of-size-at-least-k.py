#User function Template for python3

class Solution():
    def maxSumWithK(self, arr, n, k):
        # Code here
        sm=0
        maxi=-float('inf')
        for i in range(k):
            sm+=arr[i]
        maxi=max(maxi,sm)
        mini=float('inf')
        pref=0
        for i in range(k,n):
            pref+=arr[i-k]
            mini=min(mini,pref)
            sm+=arr[i]
            maxi=max(maxi,sm,sm-mini)
        return maxi
            
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        ob = Solution()
        print(ob.maxSumWithK(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends
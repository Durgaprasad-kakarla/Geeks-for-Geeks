#User function Template for python3


class Solution:

    def kthElement(self, arr, brr, k):
        l,r,n,m=0,0,len(arr),len(brr)
        while l<n and r<m:
            if arr[l]<=brr[r]:
                k-=1
                if k==0:
                    return arr[l]
                l+=1
            else:
                k-=1
                if k==0:
                    return brr[r]
                r+=1
        while l<n:
            k-=1
            if k==0:
                return arr[l]
            l+=1
        while r<m:
            k-=1
            if k==0:
                return brr[r]
            r+=1
            
         



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(a, b, k))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
#User function Template for python3

from collections import Counter
class Solution:
    def firstElementKTime(self, n, k, arr):
        # code here
        dic={}
        dic2={}
        for i in range(n):
            if arr[i] in dic:
                dic[arr[i]]+=1
            else:
                dic[arr[i]]=1
            if dic[arr[i]]==k:
                dic2[arr[i]]=i
        mini=float('inf')
        for i in range(n):
            if dic[arr[i]]>=k:
                if mini>dic2[arr[i]]:
                    mini=dic2[arr[i]]
                    ele=arr[i]
        if mini==float('inf'):
            return -1
        return ele
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, k = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstElementKTime(n, k, a))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
#User function Template for python3

# arr    : list of integers denoting the elements of the array
# target : as specified in the problem statement

class Solution:
    def threeSumClosest (self, arr, target):
        n=len(arr)
        arr.sort()
        diff=float('inf')
        closest=-float('inf')
        for i in range(n):
            if i>0 and arr[i]==arr[i-1]:
                continue
            l,r=i+1,n-1
            while l<r:
                threesum=arr[i]+arr[l]+arr[r]
                # print(i,l,r,threesum)
                if threesum==target:
                    return target
                elif threesum>target:
                    if diff>abs(threesum-target):
                        diff=abs(threesum-target)
                        closest=threesum
                    elif diff==abs(threesum-target):
                        closest=max(threesum,closest)
                    r-=1
                else:
                    if diff>abs(target-threesum):
                        diff=abs(target-threesum)
                        closest=threesum
                    elif diff==abs(target-threesum):
                        closest=max(threesum,closest)
                    l+=1
        return closest


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.threeSumClosest(A, k))

# } Driver Code Ends
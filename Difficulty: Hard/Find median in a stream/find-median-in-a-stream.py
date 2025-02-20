class MedianFinder:

    def __init__(self):
        self.arr=[]

    def addNum(self, num: int) -> None:
        l=self.binary_search(num)
        if l==len(self.arr):
            self.arr.append(num)
        else:
            self.arr.insert(l,num)

    def findMedian(self) -> float:
        n=len(self.arr)
        if n&1:
            return self.arr[n//2]
        else:
            return (self.arr[n//2]+self.arr[n//2-1])/2
    def binary_search(self,ele)->int:
        l,r=0,len(self.arr)-1
        while l<=r:
            mid=(l+r)//2
            if self.arr[mid]<=ele:
                l=mid+1
            else:
                r=mid-1
        return l

class Solution:
    def getMedian(self, arr):
        m=MedianFinder()
        medians=[]
        for i in range(len(arr)):
            m.addNum(arr[i])
            medians.append(m.findMedian())
        return medians

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.getMedian(nums)
        print(" ".join(f"{x:.1f}" for x in ans))


if __name__ == "__main__":
    main()

# } Driver Code Ends
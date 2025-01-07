#User function Template for python3
from collections import Counter

class Solution:
    def countPairs (self, nums, target) : 
        #Complete the function
        n=len(nums)
        dic=Counter(nums)
        l,r,cnt=0,n-1,0
        while l<r:
            sm=nums[l]+nums[r]
            if sm>target:
                r-=1
            elif sm<target:
                l+=1
            else:
                if nums[l]==nums[r]:
                    x=dic[nums[l]]-1
                    cnt+=(x*(x+1))//2
                else:
                    cnt+=dic[nums[l]]*dic[nums[r]]
                l+=1
                r-=1
                while l<r and nums[l]==nums[l-1]:
                    l+=1
                while l<r and nums[r]==nums[r+1]:
                    r-=1
        return cnt


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    t = int(data[0].strip())
    index = 1

    for _ in range(t):
        arr = list(map(int, data[index].strip().split()))
        index += 1
        target = int(data[index].strip())
        index += 1

        res = Solution().countPairs(arr, target)
        print(res)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
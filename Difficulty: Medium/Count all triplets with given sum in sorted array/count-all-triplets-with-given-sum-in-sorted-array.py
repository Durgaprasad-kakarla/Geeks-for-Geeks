from collections import Counter
class Solution:
    def countTriplets(self, nums, target):
        # code here
        n=len(nums)
        cnt=0
        dic=Counter(nums)
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,n-1
            while l<r:
                threesum=nums[i]+nums[l]+nums[r]
                if threesum>target:
                    r-=1
                elif threesum<target:
                    l+=1
                else:
                    x,y,z=dic[nums[i]],dic[nums[l]],dic[nums[r]]
                    if nums[i]==nums[l]:
                        if nums[l]==nums[r]:
                            k=x-1
                            cnt+=(k*(k-1)*(k+1))//6
                        else:
                            k=dic[nums[i]]-1
                            cnt+=((k*(k+1))//2)*dic[nums[r]]
                    else:
                        if nums[l]!=nums[r]:
                            cnt+=(x*y*z)
                        else:
                            k=dic[nums[r]]-1
                            cnt+=((k*(k+1))//2)*dic[nums[i]]
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and  nums[r]==nums[r+1]:
                        r-=1
        return cnt


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        target = int(input())
        ob = Solution()
        ans = ob.countTriplets(arr, target)
        print(ans)
        print("~")
# } Driver Code Ends
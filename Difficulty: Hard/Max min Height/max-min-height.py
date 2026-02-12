class Solution():
    def maxMinHeight(self, arr, k, w):
        # code here
        def check_max_height(target):
            temp = [0] * (n + 1)
            operations = 0
            curr_add = 0
            
            for i in range(n):
                curr_add += temp[i]
                
                current_height = arr[i] + curr_add
                
                if current_height < target:
                    needed = target - current_height
                    operations += needed
                    
                    if operations > k:
                        return False
                    
                    curr_add += needed
                    if i + w < n:
                        temp[i + w] -= needed
            
            return True
        n=len(arr)
        l,r,ans=min(arr),sum(arr)+k,-1
        while l<=r:
            mid=(l+r)//2
            # print(mid,check_max_height(mid))
            if check_max_height(mid):
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans
class Solution:
    def countSubarrays(self, arr, k):
        # Code here
        def kth_oddnumber(arr, k):
            left = 0
            odd_numbers = 0
            
            cnt = 0
            for r, e in enumerate(arr):
                if e&1 != 0:
                    odd_numbers += 1
                while left <= r and odd_numbers > k:
                    if arr[left]&1 != 0:
                        odd_numbers -= 1
                    left += 1
                cnt += r-left
            return cnt
        
        return kth_oddnumber(arr, k) - kth_oddnumber(arr, k-1)
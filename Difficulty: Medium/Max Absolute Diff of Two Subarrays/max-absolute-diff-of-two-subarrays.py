class Solution:
    def maxDiffSubArrays(self, arr):
        # code here
        n = len(arr)
        suffix_min = [0] * (n + 1)
        suffix_max = [0] * (n + 1)
        for i in reversed(range(n)):
            suffix_min[i] = min(suffix_min[i + 1] + arr[i], arr[i])
            suffix_max[i] = max(suffix_max[i + 1] + arr[i], arr[i])
        max_diff = abs(arr[0] - arr[1])
        prefix_min = prefix_max = arr[0]
        for i in range(1, n):
            max_diff = max(max_diff, prefix_max - suffix_min[i], suffix_max[i] - prefix_min)
            prefix_min = min(prefix_min + arr[i], arr[i])
            prefix_max = max(prefix_max + arr[i], arr[i])
        return max_diff
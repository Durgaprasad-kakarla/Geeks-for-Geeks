class Solution:
    def longestSubstr(self, s, k):
        # Code here
        freq = {}
        maxf = 0
        start = 0
        maxi = 0
    
        for end in range(len(s)):
            freq[s[end]] = freq.get(s[end], 0) + 1
            maxf = max(maxf, freq[s[end]])
    
            while (end - start + 1) - maxf > k:
                freq[s[start]] -= 1
                start += 1
    
            maxi = max(maxi, end - start + 1)
    
        return maxi
#User function Template for python3

class Solution:
    def isPallindrome(self, N):
        # code here
        return int(bin(N)[2:]==bin(N)[2:][::-1])
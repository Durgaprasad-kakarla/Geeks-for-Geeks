class Solution:
    def binstr(self, n):
        # code here
        def binary_string(ind,s):
            if ind==n:
                ans.append(s)
                return 
            binary_string(ind+1,s+'0')
            binary_string(ind+1,s+'1')
        ans=[]
        binary_string(0,'')
        return ans
        
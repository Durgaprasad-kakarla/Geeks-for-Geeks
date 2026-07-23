class Solution:
    def canRepresentBST(self, arr):
        # code here
        if not arr:
            return True
            
        stack = []
        lower_bound = -sys.maxsize - 1
        
        for i in arr:
            if i < lower_bound:
                return False
            
            while stack and i > stack[-1]:
                lower_bound = stack.pop()
            
            stack.append(i)
            
        return True
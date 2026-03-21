class Solution:
    def countBSTs(self, arr):
        # Code here
        n = len(arr)
        
        catalan = [0] * 7
        catalan[0] = catalan[1] = 1
        
        for i in range(2, 7):
            for j in range(i):
                catalan[i] += catalan[j] * catalan[i - j - 1]
        
        result = []
        
        for i in range(n):
            root = arr[i]
            left = sum(1 for x in arr if x < root)
            right = sum(1 for x in arr if x > root)
            
            result.append(catalan[left] * catalan[right])
        
        return result
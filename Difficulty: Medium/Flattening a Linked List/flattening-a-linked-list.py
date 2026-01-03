'''
class Node:
    def __init__(self, d):
        self.data=d
        self.bottom=None
        self.bottom=None
        
'''

class Solution:
    def merge(self, a, b):
        if not a:
            return b
        if not b:
            return a
            
        # Merge two lists
        if a.data < b.data:
            result = a
            result.bottom = self.merge(a.bottom, b)
        else:
            result = b
            result.bottom = self.merge(a, b.bottom)
        
        result.next = None  # Ensure the `next` pointer is null in the flattened list
        return result
    
    def flatten(self, root):
        # Base case: If the root is None or there is only one list
        if not root or not root.next:
            return root
        
        # Recursively flatten the list on the right
        root.next = self.flatten(root.next)
        
        # Merge the current list with the flattened `next` list
        root = self.merge(root, root.next)
        
        return root
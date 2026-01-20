class Solution:
    def __init__(self):
        self.stack=[]
        self.last_removed=[]
    def append(self, x):
        # append x into document
        self.stack.append(x)

    def undo(self):
        # undo last change
        self.last_removed.append(self.stack.pop())

    def redo(self):
        # redo changes
        self.stack.append(self.last_removed.pop())

    def read(self):
        # read the document
        return "".join(self.stack)
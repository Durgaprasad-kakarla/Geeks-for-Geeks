class TrieNode:
    def __init__(self):
        self.chars=[None]*26
        self.flag=False
    def contains_key(self,ch):
        return self.chars[ord(ch)-97] is not None
    def get_char(self,ch):
        return self.chars[ord(ch)-97]
    def set_char(self,ch,node):
        self.chars[ord(ch)-97]=node
    def set_end(self):
        self.flag=True
class Trie:
    def __init__(self):
        self.root=TrieNode()
        self.cnt=0
    def insert(self,word):
        n=len(word)
        for i in range(n):
            node=self.root
            for j in range(i,n):
                ch=word[j]
                if not node.contains_key(ch):
                    node.set_char(ch,TrieNode())
                    self.cnt+=1
                node=node.get_char(ch)
            node.set_end=True
    
class Solution:
    def countSubs(self, s):
        # code here
        t=Trie()
        n=len(s)
        t.insert(s)
        return t.cnt
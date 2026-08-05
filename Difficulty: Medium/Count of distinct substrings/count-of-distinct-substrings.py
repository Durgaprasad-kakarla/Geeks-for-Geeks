class TrieNode:
    def __init__(self):
        self.links=[None]*26
        self.end=False
    def contains_key(self,ch):
        return self.links[ord(ch)-ord('a')] is not None
    def put_key(self,ch,node):
        self.links[ord(ch)-ord('a')]=node
    def get_key(self,ch):
        return self.links[ord(ch)-ord('a')]
    def set_end(self):
        self.end=True
    def get_end(self):
        return self.end
class Trie:
    def __init__(self):
        self.root=TrieNode()
        self.tot=0
    def insert(self,word):
        node=self.root
        for ch in word:
            if not node.contains_key(ch):
                node.put_key(ch,TrieNode())
                self.tot+=1
            node=node.get_key(ch)
        node.set_end()


class Solution:
    def countSubs(self, word):
        # code here
        t=Trie()
        for i in range(len(word)):
            t.insert(word[i:])
        return (t.tot)
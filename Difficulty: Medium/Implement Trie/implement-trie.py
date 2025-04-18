#User function Template for python3
class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.isEndOfWord=False

class Trie:
    def __init__(self):
        # implement Trie
        self.root=TrieNode()
        
    def insert(self, key: str):
       # insert word into Trie
        temp = self.root
        for i,char in enumerate(key):
            index = ord(char) - ord('a')
            if not temp.children[index]:
                temp.children[index] = TrieNode()
            temp = temp.children[index]
            if i==len(key)-1:
                temp.isEndOfWord = True

    def search(self, key: str) -> bool:
         # search word in the Trie
        temp = self.root
        for i,char in enumerate(key):
            index = ord(char) - ord('a')
            if not temp.children[index]:
                return False
            temp = temp.children[index]
            if(i==len(key)-1 and temp.isEndOfWord):
                return True
        return False

    def isPrefix(self, key: str) -> bool:
         # search prefix word in the Trie
        temp = self.root
        for i,char in enumerate(key):
            index = ord(char) - ord('a')
            if not temp.children[index]:
                return False
            temp = temp.children[index]
        return True

#{ 
 # Driver Code Starts
def main():
    t = int(input())
    for _ in range(t):
        q = int(input())
        ans = []
        trie = Trie()

        for _ in range(q):
            x, s = input().split()
            x = int(x)

            if x == 1:
                trie.insert(s)
            elif x == 2:
                ans.append(trie.search(s))
            elif x == 3:
                ans.append(trie.isPrefix(s))

        # Print results as lowercase true/false
        print(" ".join(["true" if res else "false" for res in ans]))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
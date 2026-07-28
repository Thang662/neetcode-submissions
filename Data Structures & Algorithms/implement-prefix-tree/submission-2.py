class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isleaf = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        print(self.root.children)

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if idx not in cur.children:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]

        cur.isleaf = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            idx = ord(c) - ord('a')
            if idx not in cur.children:
                return False
            cur = cur.children[idx]

        if cur.isleaf:
            return True
            
        return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            idx = ord(c) - ord('a')
            if idx not in cur.children:
                return False
            cur = cur.children[idx]
            
        return True
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
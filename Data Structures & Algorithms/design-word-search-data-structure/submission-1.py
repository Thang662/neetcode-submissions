class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isleaf = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if idx not in cur.children:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.isleaf = True

    def search(self, word: str) -> bool:
        res = False
        def dfs(node: TrieNode, i: int):
            nonlocal res
            if i == len(word):
                if node.isleaf:
                    res = True
                return
            
            c = word[i]
            if c == '.':
                for idx in node.children:
                    dfs(node.children[idx], i+1)
            else:
                idx = ord(c) - ord('a')
                if idx in node.children:
                    dfs(node.children[idx], i+1)
        dfs(self.root, 0)
        return res                


            


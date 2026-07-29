class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.idx = -1
        self.refs = 0

    def add_word(self, word: str, index: int) -> None:
        cur = self

        for c in word:
            idx = ord(c) - ord('a')
            if idx not in cur.children:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
            cur.refs += 1
        
        cur.idx = index

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        n_rows, n_cols = len(board), len(board[0]) 
        root = TrieNode()

        for idx, word in enumerate(words):
            root.add_word(word, idx)

        def dfs(r: int, c: int, node: TrieNode) -> None:
            if r < 0 or r >= n_rows or c < 0 or c >= n_cols or board[r][c] == '*' or node is None:
                return

            tmp = board[r][c]
            board[r][c] = '*'

            idx = ord(tmp) - ord('a')
            prev = node

            if idx in node.children:
                cur = node.children[idx]
                if cur.idx != -1:
                    res.append(words[cur.idx])
                    cur.refs -= 1
                    cur.idx = -1
                    if not cur.refs:
                        prev.children.pop(idx)
                        cur = None
            else:
                cur = None
            
            dfs(r-1, c, cur)
            dfs(r+1, c, cur)
            dfs(r, c-1, cur)
            dfs(r, c+1, cur)
            board[r][c] = tmp

        for i in range(n_rows):
            for j in range(n_cols):
                dfs(i, j, root)

        print(res)
        return res
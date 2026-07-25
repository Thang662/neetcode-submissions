class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        res = False

        def dfs(r: int, c: int, i: int, path: set[int]) -> bool:
            nonlocal res
            if board[r][c] != word[i]: return
            if i == len(word)-1:
                if board[r][c] == word[i]:
                    res = True
                return
            
            for direction in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                nr, nc = r + direction[0], c + direction[1]
                idx = nr * cols + nc
                if 0 <= nr < rows and 0 <= nc < cols and idx not in path:
                    path.add(idx)
                    dfs(nr, nc, i+1, path)
                    path.remove(idx)

        for i in range(rows):
            for j in range(cols):
                print(i, j)
                dfs(i, j, 0, {i * cols + j})
        return res
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        n_rows, n_cols = len(board), len(board[0])
        remove = True

        def dfs(i: int, j: int) -> None:
            nonlocal remove
            
            if min(i, j) < 0 or i == n_rows or j == n_cols or (i, j) in visited or board[i][j] != 'O':
                return
            if min(i, j) == 0 or i == n_rows - 1 or j == n_cols -1:
                remove = False
            
            visited.add((i, j))
            tmp.append((i, j))
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        for i in range(n_rows):
            for j in range(n_cols):
                print(i, j)
                if board[i][j] == 'O' and (i, j) not in visited:
                    tmp = []
                    remove = True
                    dfs(i, j)
                    if remove:
                        for r, c in tmp:
                            board[r][c] = 'X'

        



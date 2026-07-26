class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for i in range(n)]
        res = []

        def dfs(r: int) -> None:
            if r == n:
                res.append([''.join(row) for row in board])
                return

            for i in range(n):
                board[r][i] = 'Q'
                if self.check(r, i, board):
                    dfs(r+1)
                board[r][i] = '.'
        dfs(0)
        print(res)
        return res
        
    def check(self, r: int, c: int, board: List[List[str]]) -> bool:
        row = r - 1
        while row >= 0:
            if board[row][c] == 'Q':
                return False
            row -= 1
        
        row, col = r - 1, c - 1
        while row >= 0 and col >= 0:
            if board[row][col] == 'Q':
                return False
            row, col = row - 1, col - 1

        row, col = r - 1, c + 1
        while row >= 0 and len(board) > col:
            if board[row][col] == 'Q':
                return False
            row, col = row - 1, col + 1
        return True
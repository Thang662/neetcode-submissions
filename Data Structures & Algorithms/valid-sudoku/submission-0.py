class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for r in range(9):
            for c in range(9):
                
                if board[r][c] != '.':
                    b = r // 3 * 3 + c // 3
                    if (board[r][c] in rows[r]) or (board[r][c] in cols[c]) or (board[r][c] in boxes[b]):
                        return False
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    boxes[b].add(board[r][c])

        return True
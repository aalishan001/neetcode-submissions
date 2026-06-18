class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_hash = defaultdict(set)
        row_hash = defaultdict(set)
        square_hash = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    if (board[r][c] in col_hash[c] or board[r][c] in row_hash[r] or board[r][c] in square_hash[(r//3,c//3)]):
                        return False
                    col_hash[c].add(board[r][c])
                    row_hash[r].add(board[r][c])
                    print(r//3,c//3)
                    square_hash[(r//3,c//3)].add(board[r][c])
        return True
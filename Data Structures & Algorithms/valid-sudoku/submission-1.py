class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # using defaultdict(set) instead of {}
        # unlike {}, it returns non existing keys as blank
        rowHash = defaultdict(set)
        colHash = defaultdict(set)
        sqrHash = defaultdict(set)
        # iterate through board
        for r in range(9):
            for c in range(9):
                # skip blanks
                if board[r][c] == ".":
                    continue
                # check if that number is already in a row, col, or square
                # using "// 3" helps make the square
                if (board[r][c] in rowHash[r]
                    or board[r][c] in colHash[c]
                    or board[r][c] in sqrHash[r // 3, c // 3]):
                    return False
                # add to the hash   
                rowHash[r].add(board[r][c])
                colHash[c].add(board[r][c])
                sqrHash[(r // 3, c // 3)].add(board[r][c])
        # return true if the loop ends
        return True
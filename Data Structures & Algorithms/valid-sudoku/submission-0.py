class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check 3x3 boxes
        for box_row in range(3):  # Which row of boxes (0, 1, or 2)
            for box_col in range(3):  # Which column of boxes (0, 1, or 2)
                group_1 = []  # Reusing your variable name for each 3x3 box
                for i in range(3):  # Row within the box
                    for j in range(3):  # Column within the box
                        # Calculate actual board position
                        row = box_row * 3 + i
                        col = box_col * 3 + j
                        
                        if board[row][col] != ".":
                            if board[row][col] in group_1:
                                return False
                            group_1.append(board[row][col])
        
        # Check rows
        for i in range(9):
            group_2 = []  # Reusing your variable name for row checking
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in group_2:
                        return False
                    group_2.append(board[i][j])
        
        # Check columns
        for j in range(9):
            group_3 = []  # Reusing your variable name for column checking
            for i in range(9):
                if board[i][j] != ".":
                    if board[i][j] in group_3:
                        return False
                    group_3.append(board[i][j])
        
        return True

                    





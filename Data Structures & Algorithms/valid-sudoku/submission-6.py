class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_row = []
        seen_col = []
        box = [[[], [], []], [[], [], []], [[], [], []]]

        for i in range(9):
            box_height = i // 3

            for j in range(9):
                box_width = j // 3
                
                if (board[i][j].isdigit() 
                    and ( board[i][j] in seen_row
                    or board[i][j] in box[box_height][box_width])): 
                    return False

                if board[j][i].isdigit() and board[j][i] in seen_col:
                    return False
                
                box[box_height][box_width].append(board[i][j])
                seen_row.append(board[i][j])
                seen_col.append(board[j][i])                

            seen_row.clear()
            seen_col.clear()

        return True



        
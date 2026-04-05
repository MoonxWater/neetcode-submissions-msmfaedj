class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        create a hashmap with keys being the container to check 
        and values being the present numbers within that container

        to access the container:
            the row: simple 2-d traversal [i][j to end]
            the column: [i to end][j]
            while performing the above, why not store the values in a 
            container to simulate "box" of the sudoku and then traverse
            it in the end
            the box: becomes a simple 1-d traversal
            box = [ 0-2[0-2[], 3-5[], 6-8[]], 
                    3-5[0-2[], 3-5[], 6-8[]], 
                    6-8[0-2[], 3-5[], 6-8[]]
                  ]

        '''

        seen_row = []
        seen_col = []

        for i in range(9):
            for j in range(9):
                # validate row
                if board[i][j].isdigit() and board[i][j] in seen_row:
                    return False
                elif board[i][j].isdigit():
                    seen_row.append(board[i][j])

                # validate column
                if board[j][i].isdigit() and board[j][i] in seen_col:
                    return False
                elif board[j][i].isdigit():
                    seen_col.append(board[j][i])                

            seen_row = []
            seen_col = []
        
        del seen_row
        del seen_col
        
        box = [[[], [], []], [[], [], []], [[], [], []],]

        for i in range(9):
            box_height = i // 3
            for j in range(9):
                box_width = j // 3
                if board[i][j].isdigit() and board[i][j] in box[box_height][box_width]:
                    return False
                elif board[i][j].isdigit():
                    box[box_height][box_width].append(board[i][j])
        return True



        
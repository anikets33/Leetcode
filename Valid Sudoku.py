class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = []
            col = []
            for j in range(9):
                if board[i][j] != '.':  row.append(board[i][j])
                if board[j][i] != '.':  col.append(board[j][i])
            if len(set(row)) != len(row) or len(set(col)) != len(col):
                return False 
            
        i = 0
        a,b,c = [],[],[]
        while i<9:
            j = 0
            while j<3:
                if board[i][j] != '.':  a.append(board[i][j])
                if board[i][j+3] != '.':  b.append(board[i][j+3])
                if board[i][j+6] != '.':  c.append(board[i][j+6])
                j += 1
            i += 1
            if i == 3 or i == 6 or i == 9:
                if len(set(a)) != len(a) or len(set(b)) != len(b) or len(set(c)) != len(c):
                    return False
                a,b,c =[],[],[]
            
        return True
                

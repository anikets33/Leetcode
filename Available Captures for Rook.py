class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook = []
        count = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rook = [i, j]
                    
        move = rook[1] - 1  
        while move>=0:
            if board[rook[0]][move] == 'p':
                count += 1
                break
            if board[rook[0]][move] == 'B':
                break
            move -= 1
        move = rook[1] + 1
        while move<8:
            if board[rook[0]][move] == 'p':
                count += 1
                break
            if board[rook[0]][move] == 'B':
                break
            move += 1
        move = rook[0] - 1
        while move>=0:
            if board[move][rook[1]] == 'p':
                count += 1
                break
            if board[move][rook[1]] == 'B':
                break
            move -= 1
        move = rook[0] + 1
        while move<8:
            if board[move][rook[1]] == 'p':
                count += 1
                break
            if board[move][rook[1]] == 'B':
                break
            move += 1
        
        return count

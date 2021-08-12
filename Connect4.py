from enum import Enum
class Piece_State(Enum):
    EMPTY = 0
    RED = 1
    YELLOW = 2

class Piece:
    def __init__(self, piece_status = Piece_State.EMPTY):
        self.state = piece_status # Defaults to empty, helpful when initializing the board


class Board:
    # board coordinates: (0,0) is bottom left; (6,5) is top right
    def __init__(self):
        self.board = [] #7 across, 6 tall
        for i in range(0,7): # 7 across
            for j in range(0,6):
                self.board[i][j] = Piece()

    def check_win(self, row, column): # looks for a connect 4 around a specific piece
        #should only be called in the insert_piece function; after each piece has been placed
        
        #check column
        consecutive_pieces = 0
        for j in range(row, -1, -1): # iterates from the top of the column to the bottom, looking for 4 in a line
            if self.board[column][j].piece_status != self.board[column][j - 1].piece_status: # if there are two sequential, consecutive, non-matching pieces, reset the counter
                consecutive_pieces = 0
            else: # else, mark that there is another consecutive piece
                consecutive_pieces += 1
                if consecutive_pieces >= 4: # if 4 or more pieces are in a line, return that a win has occured (True)
                    return True

        #check row
        for i in range(0, 7): # iterates from the right of the row to the left, looking for 4 in a line
            if self.board[i][row].piece_status != self.board[i + 1][row].piece_status: # if there are two sequential, consecutive, non-matching pieces, reset the counter
                consecutive_pieces = 0
            else: # else, mark that there is another consecutive piece
                consecutive_pieces += 1
                if consecutive_pieces >= 4: # if 4 or more pieces are in a line, return that a win has occured (True)
                    return True

        #check negative slope diagonal

        
        
        
        
        return False






    def insert_piece(self, piece_status, column):
        flag = False # flag to check if a piece has been inserted
        j = 0 # iterator through the list; TODO LOOK FOR BETTER WAY TO ITERATE THROUGH LIST HERE
        while flag == False and j < 6: # iterate from the bottom up in the column the player wants to put a piece in
            if self.board[column][j] == Piece_State.EMPTY: # if the spot is empty, enter the piece
                self.board[column][j] = piece_status
                flag = True
            j += 1
        
        if flag == False: # if the function has reached the top of the column without placing a piece, the column was full
            print("Invalid Move: Column already full.")
        return







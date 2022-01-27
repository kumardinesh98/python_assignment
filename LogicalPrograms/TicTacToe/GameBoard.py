class GameBoard:
    board = ["-" for count in range(9)]
    def play_board(self,board):
        print(f'|', board[0], '|', board[1], '|', board[2])
        print(f'|', board[3], '|', board[4], '|', board[5])
        print(f'|', board[6], '|', board[7], '|', board[8])


    def display_board(self):
        self.play_board(self.board)

    def set_board(self,position,player):
        if self.board[position -1] == "-":
            self.board[position -1] = player
            return True
        return False

    def check_win(self, player):
        win_positions = [[0,1,2],[3,4,5],[6,7,8,],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

        for check in win_positions:
            if (self.board[check[0]] == player) and (self.board[check[1]] == player) and (self.board[check[2]] == player) :
                return True
        return False

    def check_tie(self):
        if "-" not in self.board:
            return True
        return False
    def check_move(self,step):
        if step in self.board:
            return True
        return False



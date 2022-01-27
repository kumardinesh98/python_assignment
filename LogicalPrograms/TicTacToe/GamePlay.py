import random

from LogicalPrograms.TicTacToe.GameBoard import GameBoard


class GamePlay:
    PLAYER = "X"
    COMPUTER = "Y"

    def play_game(self):
        game_board = GameBoard()
        exit = False
        while not exit:

            while True:
                try:
                    if game_board.check_tie():
                        print("match has been tied")
                        exit = True
                        break
                    step = int(input(F"{self.PLAYER} enter your position"))
                    if step not in range(1, 10):
                        raise Exception

                    if not game_board.set_board(step, self.PLAYER):
                        print("this position is engaged.please try another")
                        continue

                    game_board.display_board()
                    if game_board.check_win(self.PLAYER):
                        print("player won the game")
                        exit = True
                        break
                    break

                except Exception:
                    print("please enter a valid number [1-9]")

            if exit:
                break

            while True:
                if game_board.check_tie():
                    print("match has been tied")
                    exit = True
                    break
                print("computer move")
                while True:
                    step = random.randint(1, 9)
                    if game_board.set_board(step, self.COMPUTER):
                        break

                game_board.set_board(step, self.COMPUTER )
                game_board.display_board()
                if game_board.check_win(self.COMPUTER):
                    print("computer won the game")
                    exit = True
                    break
                break


game_play = GamePlay()
game_play.play_game()

from LogicalPrograms.Gambler.Game import Game


class Player:
    def requirments(self):
        while True:

            try:
                amount = float(input("enter the amount "))
                target = float(input("enter the target"))
                if amount < 0 or target < 0:
                    raise ValueError
                game = Game(amount, target)
                game.game_play()
                print(game)
                break
            except ValueError:
                print("please enter a valid number")

start_game = Player()
start_game.requirments()
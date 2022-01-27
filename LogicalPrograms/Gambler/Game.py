import random


class Game:

    def __init__(self, amount, target):
        self.amount = amount
        self.target = target
        self.count = 0
        self.result = None
        self.win_percent = 0
        self.lost_percent = 0


    def random_number(self):
        return random.randint(1,2)

    def find_result(self, amount):
        if amount == self.target:
            return "gambler won the game"
        else:
            return "gambler lost the game"

    def find_percent(self, value):
        return round((value/self.count)*100,2)


    def game_play(self):
        win = 0
        lose = 0
        while(self.amount != 0 )and (self.amount != self.target):
            play1 = self.random_number()
            play2 = self.random_number()
            if(play1 == play2):
                self.amount +=1
                win +=1
            else:
                self.amount -=1
                lose +=1
            self.count +=1
        self.result = self.find_result(self.amount)
        self.win_percent = self.find_percent(win)
        self.lost_percent = self.find_percent(lose)

    def __str__(self):
        return f"amount balance :{self.amount}\ntargeted amount :{self.result}\ntotal count :{self.count}\n" \
               f"game result :{self.result}\nwin percent :{self.win_percent}\nlost percent :{self.lost_percent}"
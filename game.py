from player import Player
from robot import Robot
test = Robot()

class Game:
    def __init__(self):
        pass

    def display_welcome(self): #tested
        print('Welcome to Rock Paper Scissors Lizard Spock! The greatest game you only heard of and always wanted to play.\n\nThe rules are similar to Rock, Paper, Scissors, but with an added twist: Lizard and Spock!\n')

        print('Here’s how to win (and lose): \n\nRock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock\n')

        print('Winning a round will give you one point.\nThe goal is to have 2 wins to beat your opponent.\n')

    def game_type(self): #tested
        self.user_input = int(input('Type [1] for a single player game.\nType [2] for a double player game.\n'))
        if self.user_input == 1 or 2: #temporary
            self.single_player_game()
        print('Let\'s Begin!')



    def single_player_game(self):
        pass

        

    def run_game(self):
        self.display_welcome()
        self.game_type()
        test.choose_gesture()
        
        

    
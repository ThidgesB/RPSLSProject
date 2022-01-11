from robot import Robot
from human import Human
import sys

class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None
        self.player_one.player_order = 1

    def input_check(self, message):
        while True:
            try:
                user_input = int(input(message))
            except ValueError:
                print("Please enter a number")
                continue
            else:
                return user_input

    def display_welcome(self): #tested
        print('Welcome to Rock Paper Scissors Lizard Spock! The greatest game you only heard of and always wanted to play.\n\nThe rules are similar to Rock, Paper, Scissors, but with an added twist: Lizard and Spock!\n')

        print('Here’s how to win (and lose): \n\nRock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock\n')

        print('Winning a round will give you one point.\nThe goal is to have 2 wins to beat your opponent.\n')

    def game_type(self): #tested
        user_input = self.input_check('Type [1] for a single player game.\nType [2] for a co-op game.\n') 
        if user_input == 1:
            self.player_two = Robot()
            self.game_round()
            # self.single_player_game()
        elif user_input == 2:
            self.player_two = Human()
            self.player_two.player_order = 2
            self.game_round()
        else:
            print('Incorrect input')
            self.game_type()

    # def single_player_game(self):
    #     self.game_round()


    def game_round(self):
        self.compare_gestures(self.player_one.choose_gesture(), self.player_two.choose_gesture())
        self.show_score()

    def run_game(self):
        self.display_welcome()
        self.game_type()
        #self.game_round()
        #restart game?

    def compare_gestures(self, human_choice, computer_choice):
        if human_choice == computer_choice:
            print('It\'s a tie!')
            self.game_round()
        elif ((human_choice == 0) and (computer_choice == 2 or computer_choice == 3)) or ((human_choice == 1) and (computer_choice == 0 or computer_choice == 4)) or ((human_choice == 2) and (computer_choice == 1 or computer_choice == 3)) or ((human_choice == 3) and (computer_choice == 4 or computer_choice == 1)) or ((human_choice == 4) and (computer_choice == 2 or computer_choice == 0)):
            self.player_one.player_one_score += 1
            print('\nPlayer One wins this round!\n')  
            return self.player_one.player_one_score 
        else: 
            self.player_two.player_two_score += 1
            print('\nPlayer Two wins this round!\n') 
            return self.player_two.player_two_score
    

    def show_score(self):
        print(f'Player One : {self.player_one.player_one_score}  |  Player Two: {self.player_two.player_two_score}')
        self.declare_winner()

    def declare_winner(self):
            if self.player_one.player_one_score != 2 and self.player_two.player_two_score != 2:
                self.game_round()

            elif self.player_one.player_one_score == 2:
                print('Player One wins the game!')
                sys.exit()

            elif self.player_two.player_two_score == 2:
                print('Player Two wins the game!')
                sys.exit()

#bonus: play again function
        
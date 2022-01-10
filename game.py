from player import Player
from robot import Robot
from human import Human
robot = Robot()
human = Human()

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
            human.choose_gesture(self)
            robot.choose_gesture(self)
            self.compare_gestures(self)     #compare gestures
            pass

    def game_round(self):
        self.compare_gestures(human.choose_gesture(), robot.choose_gesture())
        self.show_score()

    def run_game(self):
        self.display_welcome()
        # self.game_type()
        self.game_round()
        #restart game?

    def compare_gestures(self, human_choice, computer_choice):
        if human_choice == computer_choice:
            print('It\'s a tie!')
            self.single_player_game()
        elif ((human_choice == 0) and (computer_choice is 2 or 3)) or ((human_choice == 1) and (computer_choice is 0 or 4)) or ((human_choice == 2) and (computer_choice is 1 or 3)) or ((human_choice == 3) and (computer_choice is 4 or 1)) or ((human_choice == 4) and (computer_choice is 2 or 0)):
            human.human_score += 1
            print('Player One wins this round!')  
            return human.human_score 
        else: 
            robot.robot_score += 1
            print('Player Two wins this round!') 
            return robot.robot_score
    

    def show_score(self):
        print(f'Player One : {human.human_score}  |  Player Two: {robot.robot_score}')
        self.declare_winner()

    def declare_winner(self):
        self.game_over = False
        while self.game_over == False:
            self.game_round()
            if (human.human_score) and (robot.robot_score) != 2:
                self.game_over = False
            elif human.human_score == 2:
                print('Player One wins the game!')
                self.game_over = True
            elif robot.robot_score == 2:
                print('Player Two wins the game!')
                self.game_over = True


#bonus: play again function
        
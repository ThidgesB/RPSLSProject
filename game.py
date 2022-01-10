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
        self.game_over = False
        while self.game_over == False:
            human.choose_gesture(self)
            robot.choose_gesture(self)
            self.compare_gestures(self)     #compare gestures

        pass

        

    def run_game(self):
        self.display_welcome()
        # self.game_type()
        # human.choose_gesture()
        # robot.choose_gesture() #temporary
        self.compare_gestures(human.choose_gesture(), robot.choose_gesture())
        self.show_score()


    def compare_gestures(self, human_choice, computer_choice):
        
        if human_choice > computer_choice:
            human.human_score += 1

            return(human.human_score)
        
        elif human_choice == computer_choice:
            print('It\'s a tie!')
            self.single_player_game()

        else:
            robot.robot_score += 1
            return (robot.robot_score)
    

    def show_score(self):
        if human.human_score == 2:
            print("Player One is the winner!")
            self.game_over == True
            
        elif robot.robot_score == 2:
            print("Player Two is the winner!")
            self.game_over == True  
        
        else:
            print(f'Player One : {human.human_score}  |  Player Two: {robot.robot_score}')
            self.game_over = False            


#bonus: play again function
        
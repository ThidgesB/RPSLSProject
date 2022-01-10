 #REVISED def compare_gestures for Game Class

def compare_gestures(self, human_choice, computer_choice):
      
  if human_choice == computer_choice:
    print('It\'s a tie!')
    self.single_player_game()
    
  elif ((human_choice == 0) and (computer_choice is 2 or 3)) or ((human_choice == 1) and (computer_choice is 0 or 4)) or ((human_choice == 2) and (computer_choice is 1 or 3)) or ((human_choice == 3) and (computer_choice is 4 or 1)) or ((human_choice == 4) and (computer_choice is 2 or 0)):
    self.human_score += 1
    print('Player One win!')  
    return self.human_score 

  else: 
    self.robot_score += 1
    print('Player Two wins!') 
    return self.robot_score
from player import Player
import random

class Robot(Player):
  def __init__(self):
    self.robot_score = 0
    self.name = ('Player Two')

    super().__init__()

  def choose_gesture(self):
    self.robot_choice = self.random_selection(self.gesture_list)    #Tested, works. Returns random selection from gesture list
    return self.robot_choice

  def random_selection(self, selection):
      random_index = random.randint(0,len(selection)-1)
      result = selection[random_index]
      print(result)
      return result  


    #import random
    #create the list
    #
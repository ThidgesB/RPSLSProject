from player import Player

class Human(Player):
  def __init__(self):
    self.name = ('Player One')
    self.human_score = 0
    super().__init__()

  def choose_gesture(self):
    self.show_gesture()
    self.user_input = int(input('Please choose a gesture: '))
    #self.user_input = int(input('Please choose a gesture: '))
    #self.user_choice = index[self.user_input]
    return self.user_input            #return user input
    

  def show_gesture(self):
    self.temp_index = 0       #test index
    for gesture in self.gesture_list:
      print(f'Press [{self.temp_index}] for {gesture}')
      self.temp_index += 1


  def test(self):
    print(self.score)
from player import Player

class Human(Player):
  def __init__(self):
    self.name = ('Player One')
    self.player_one_score = 0
    self.player_two_score = 0
    super().__init__()

  def input_check(self, message):
        while True:
            try:
                user_input = int(input(message))
            except ValueError:
                print("Please enter a number")
                continue
            else:
                return user_input


  def choose_gesture(self):
    self.show_gesture()
    self.user_input = self.input_check('\nPlease choose a gesture: ')
    #self.user_input = int(input('Please choose a gesture: '))
    #self.user_choice = index[self.user_input]
    return self.user_input            #return user input
    

  def show_gesture(self):
    print('')
    self.temp_index = 0       #test index
    for gesture in self.gesture_list:
      print(f'Press [{self.temp_index}] for {gesture}')
      self.temp_index += 1


  def test(self):
    print(self.score)
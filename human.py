from player import Player

class Human(Player):
  def __init__(self):
    self.name = ('Player One')
    super().__init__()

  def choose_gesture(self):
    self.user_input = int(input('Please choose a gesture: '))
    self.temp_index = 0
    for gesture in self.gesture_list:
      print(f'Press [{self.temp_index}] for {gesture}')
      self.temp_index += 1

  def test(self):
    print(self.score)
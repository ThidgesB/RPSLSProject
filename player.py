class Player:
  def __init__(self, score):
    self.gesture_list = ['Rock', 'Paper', 'Scissors']  #add lizard and Spock when we've figured this out
    self.score = 0
    pass

  def choose_gesture(self):
    self.user_input = int(input('Please choose a gesture: '))
    self.temp_index = 0
    for gesture in self.gesture_list:
      print(f'Press [{self.temp_index}] for {gesture}')
      self.temp_index += 1
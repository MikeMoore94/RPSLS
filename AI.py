from player import Player
import random 

class AI(Player):
    def __init__(self):
        self.name = "alfred"
        super().__init__()

    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.gestures)
        
from ai import AI
from human import Human

class Game:
    def __init__(self):
        self.player_one = Human
        self.player_two = None
        # self.player_one.score = 0
        # self.player_two.score = 0

    def run_game(self):
        self.game_rules()
        self.multiplayer()
        
        # while self.player_one.score < 2 or self.player_two.score < 2:
        #     self.play_game()

        self.display_winner()

    def game_rules(self):
        print("welcome to Rock, Paper, Scissors, Lizard, Spock, the game of chance")
        print("The rules are similar to the childrens game Rock, Paper, Scissors")
        print("The gestures are: Rock, Paper, Scissors, Lizard, Spock")
        print("Rock crushes Scissors \nScissors cuts paper \nPaper covers Rock \nRock crushes Lizard \nLizard poisons Spock \nSpock smashes Scissors \nScissors decapitates Lizard \nLizard eats Paper \nPaper diproves Spock \nSpock vaporizes Rock")

    


    def multiplayer(self):
        user_input = input("If you want to play singleplayer press 1 \nFor multiplayer press 2")
        if user_input == "1":
            self.player_one.name = input("Player 1 , enter your name: ")
            self.player_one = Human()
            self.player_two = AI()
        elif user_input == "2":
            self.player_one.name = input("Player 1, enter your name")
            self.player_one = Human()
            self.player_two.name = input("Player 2, enter your name")
            self.player_two = Human()
        else:
            input("please enter 1 for single player or 2 for multiplayer")

    def player_chosen(self):
        print(f"{self.player_one.name} picked {self.player_one.chosen_gesture}")
        print(f"{self.player_two.name} picked {self.player_two.chosen_gesture}")


    def play_game(self):
        #call on player class to choose gesture
        #call player_chosen method
        #if else for all possible outcomes 
        pass

    def display_winner(self):
        if self.player_one.score == 2:
            print(f"{self.player_one.name} wins the game")

        elif self.player_two.score == 2:
            print(f"{self.player_two.name} wins the game")

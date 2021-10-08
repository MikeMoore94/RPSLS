from ai import AI
from human import Human

class Game:
    def __init__(self):
        self.player_one = Human
        self.player_two = None
        

    def run_game(self):
        self.game_rules()
        self.multiplayer()
        
        while self.player_one.score < 3 and self.player_two.score < 3:
            self.play()

        self.diaplay_winner()

    def game_rules(self):
        print("welcome to Rock, Paper, Scissors, Lizard, Spock, the game of chance")
        print("The rules are similar to the childrens game Rock, Paper, Scissors")
        print("The gestures are: Rock, Paper, Scissors, Lizard, Spock")
        print("Rock crushes Scissors n\ Scissors cuts paper n\ Paper covers Rock n\ Rock crushes Lizard n\ Lizard poisons Spock n\ Spock smashes Scissors n\ Scissors decapitates Lizard n\ Lizard eats Paper n\ Paper diproves Spock n\ Spcok vaporizes Rock")

    


    def multiplayer(self):
        #ask what player name is
        #ask if how many players there are
        #method for if one player
        #method for two players 
        pass

    def player_chosen(self):
        #show what each player picked for said round 
        pass

    def play_game(self):
        #call on player class to choose gesture
        #call player_chosen method
        #if else for all possible outcomes 
        pass

    def display_winner(self):
        #logic for if someone gets more then two wins they are the winner
        pass
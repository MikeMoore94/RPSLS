from ai import AI
from human import Human
from humantwo import HumanTwo

class Game:
    def __init__(self):
        self.player_one = Human
        self.player_two = HumanTwo
        self.player_one_win = 0
        self.player_two_win = 0
        self.draw = 0
        self.ai_win = 0

    def run_game(self):
        self.game_rules()
        self.multiplayer()
        

    def game_rules(self):
        print("welcome to Rock, Paper, Scissors, Lizard, Spock, the game of chance")
        print("The rules are similar to the childrens game Rock, Paper, Scissors")
        print("The gestures are: Rock, Paper, Scissors, Lizard, Spock")
        print("Rock crushes Scissors \nScissors cuts paper \nPaper covers Rock \nRock crushes Lizard \nLizard poisons Spock \nSpock smashes Scissors \nScissors decapitates Lizard \nLizard eats Paper \nPaper diproves Spock \nSpock vaporizes Rock")

    


    def multiplayer(self):
        user_input = input("If you want to play singleplayer press 1 \nFor multiplayer press 2 ")
        if user_input == "1":
            self.player_one = Human()
            self.player_one.name = input("Player 1 , enter your name: ")
            self.ai = AI()
        elif user_input == "2":
            self.player_one = Human()
            self.player_one.name = input("Player 1, enter your name: ")
            self.player_two = HumanTwo()
            self.player_two.name = input("Player 2, enter your name: ")
        else:
            input("please enter 1 for single player or 2 for multiplayer")
        self.play_game(user_input)

    def player_chosen(self):
        print(f"{self.player_one.name} picked {self.player_one.chosen_gesture} ")
        print(f"{self.player_two.name} picked {self.player_two.chosen_gesture} ")

    def ai_chosen(self):
        print(f"{self.player_one.name} picked {self.player_one.chosen_gesture} ")
        print(f"{self.ai.name} picked {self.ai.chosen_gesture} ")



    def play_game(self, game_type):
        if game_type == "2":
            while self.player_one_win <= 2 or self.player_two_win <= 2:
                self.player_one.choose_gesture()
                self.player_two.choose_gesture()
                
                if self.player_one.chosen_gesture == "rock" and self.player_two.chosen_gesture == "paper":
                    self.player_two_win += 1
                    print("paper covers rock")
                elif self.player_one.chosen_gesture == "rock" and self.player_two.chosen_gesture == "sissors":
                    self.player_chosen()
                    self.player_one_win += 1
                    print("rock smashes sissors")
                elif self.player_one.chosen_gesture == "rock" and self.player_two.chosen_gesture == "lizard":
                    self.player_chosen()
                    self.player_one_win += 1
                    print("rock smashes lizard")
                elif self.player_one.chosen_gesture == "rock" and self.player_two.chosen_gesture == "spock":
                    self.player_chosen()
                    self.player_two_win += 1
                    print("spock destroys rock")
                elif self.player_one.chosen_gesture == "rock" and self.player_two.chosen_gesture == "rock":
                    self.player_chosen()
                    self.draw += 1
                    print("draw")
                elif self.player_one.chosen_gesture == "paper" and self.player_two.chosen_gesture == "rock":
                    self.player_chosen()
                    self.player_one_win += 1
                    print("paper covers rock")
                elif self.player_one.chosen_gesture == "paper" and self.player_two.chosen_gesture == "sissors":
                    self.player_chosen()
                    self.player_two_win += 1
                    print("sissors cut paper")
                elif self.player_one.chosen_gesture == "paper" and self.player_two.chosen_gesture == "lizard":
                    self.player_chosen()
                    self.player_two_win += 1
                    print("lizard eats paper")
                elif self.player_one.chosen_gesture == "paper" and self.player_two.chosen_gesture == "spock":
                    self.player_chosen()
                    self.player_one_win += 1
                    print("paper confuses spock")
                elif self.player_one.chosen_gesture == "paper" and self.player_two.chosen_gesture == "paper":
                    self.player_chosen()
                    self.draw += 1
                    print("draw")
                elif self.player_one.chosen_gesture == "sissors" and self.player_two.chosen_gesture == "paper":
                    self.player_chosen()
                    self.player_one_win += 1
                    print("sissors cut paper")
                elif self.player_one.chosen_gesture == "sissors" and self.player_two.chosen_gesture == "rock":
                    self.player_chosen()
                    self.player_two_win += 1
                    print("rock smashes sissors")
                elif self.player_one.chosen_gesture == "sissors" and self.player_two.chosen_gesture == "lizard":
                    self.player_chosen()
                    self.player_one_win += 1
                    print("sissors cut lizards head off")
                elif self.player_one.chosen_gesture == "sissors" and self.player_two.chosen_gesture == "spock":
                    self.player_chosen()
                    self.player_two_win += 1
                    print("spock smashes sissors")
                elif self.player_one.chosen_gesture == "sissors" and self.player_two.chosen_gesture == "sissors":
                    self.player_chosen()
                    self.draw += 1
                    print("draw")
                elif self.player_one.chosen_gesture == "lizard" and self.player_two.chosen_gesture == "rock":
                    self.player_chosen()
                    self.player_two_win += 1
                    print("rock smashes lizard")
                elif self.player_one.chosen_gesture == "lizard" and self.player_two.chosen_gesture == "sissors":
                    self.player_chosen()
                    self.player_two_win += 1
                    print("sissors cut lizard")
                elif self.player_one.chosen_gesture == "lizard" and self.player_two.chosen_gesture == "paper":
                    self.player_chosen()
                    self.player_one_win += 1
                    print("lizard eats paper")
                elif self.player_one.chosen_gesture == "lizard" and self.player_two.chosen_gesture == "spock":
                    self.player_chosen()
                    self.player_one_win += 1
                    print("lizard poisons spock")
                elif self.player_one.chosen_gesture == "lizard" and self.player_two.chosen_gesture == "lizard":
                    self.player_chosen()
                    self.draw += 1
                    print("draw")
                elif self.player_one.chosen_gesture == "spock" and self.player_two.chosen_gesture == "rock":
                    self.player_chosen()
                    self.player_one_win += 1
                    print("spock smashes rock")
                elif self.player_one.chosen_gesture == "spock" and self.player_two.chosen_gesture == "sissors":
                    self.player_chosen()
                    self.player_one_win += 1
                    print("spock smashes sissors")
                elif self.player_one.chosen_gesture == "spock" and self.player_two.chosen_gesture == "paper":
                    self.player_chosen()
                    self.player_two_win += 1
                    print("paper confuses spock")
                elif self.player_one.chosen_gesture == "spock" and self.player_two.chosen_gesture == "lizard":
                    self.player_chosen()
                    self.player_two_win += 1
                    print("lizard poisons spock")
                elif self.player_one.chosen_gesture == "spock" and self.player_two.chosen_gesture == "spock":
                    self.player_chosen()
                    self.draw += 1
                    print("draw")
        
        elif game_type == "1":
            while self.player_one_win <= 2 or self.ai_win <= 2:
                self.player_one.choose_gesture()
                self.ai.choose_gesture()

                if self.player_one.chosen_gesture == "rock" and self.ai.chosen_gesture == "paper":
                    self.ai_chosen()
                    self.ai_win += 1
                    print("paper covers rock")
                elif self.player_one.chosen_gesture == "rock" and self.ai.chosen_gesture == "sissors":
                    self.ai_chosen()
                    self.player_one_win += 1
                    print("rock smashes sissors")
                elif self.player_one.chosen_gesture == "rock" and self.ai.chosen_gesture == "lizard":
                    self.ai_chosen()
                    self.player_one_win += 1
                    print("rock smashes lizard")
                elif self.player_one.chosen_gesture == "rock" and self.ai.chosen_gesture == "spock":
                    self.ai_chosen()
                    self.ai_win += 1
                    print("spock destroys rock")
                elif self.player_one.chosen_gesture == "rock" and self.ai.chosen_gesture == "rock":
                    self.ai_chosen()
                    self.draw += 1
                    print("draw")
                elif self.player_one.chosen_gesture == "paper" and self.ai.chosen_gesture == "rock":
                    self.ai_chosen()
                    self.player_one_win += 1
                    print("paper covers rock")
                elif self.player_one.chosen_gesture == "paper" and self.ai.chosen_gesture == "sissors":
                    self.ai_chosen()
                    self.ai_win += 1
                    print("sissors cut paper")
                elif self.player_one.chosen_gesture == "paper" and self.ai.chosen_gesture == "lizard":
                    self.ai_chosen()
                    self.ai_win += 1
                    print("lizard eats paper")
                elif self.player_one.chosen_gesture == "paper" and self.ai.chosen_gesture == "spock":
                    self.ai_chosen()
                    self.player_one_win += 1
                    print("paper confuses spock")
                elif self.player_one.chosen_gesture == "paper" and self.ai.chosen_gesture == "paper":
                    self.ai_chosen()
                    self.draw += 1
                    print("draw")
                elif self.player_one.chosen_gesture == "sissors" and self.ai.chosen_gesture == "paper":
                    self.ai_chosen()
                    self.player_one_win += 1
                    print("sissors cut paper")
                elif self.player_one.chosen_gesture == "sissors" and self.ai.chosen_gesture == "rock":
                    self.ai_chosen()
                    self.ai_win += 1
                    print("rock smashes sissors")
                elif self.player_one.chosen_gesture == "sissors" and self.ai.chosen_gesture == "lizard":
                    self.ai_chosen()
                    self.player_one_win += 1
                    print("sissors cut lizards head off")
                elif self.player_one.chosen_gesture == "sissors" and self.ai.chosen_gesture == "spock":
                    self.ai_chosen()
                    self.ai_win += 1
                    print("spock smashes sissors")
                elif self.player_one.chosen_gesture == "sissors" and self.ai.chosen_gesture == "sissors":
                    self.ai_chosen()
                    self.draw += 1
                    print("draw")
                elif self.player_one.chosen_gesture == "lizard" and self.ai.chosen_gesture == "rock":
                    self.ai_chosen()
                    self.ai_win += 1
                    print("rock smashes lizard")
                elif self.player_one.chosen_gesture == "lizard" and self.ai.chosen_gesture == "sissors":
                    self.ai_chosen()
                    self.ai_win += 1
                    print("sissors cut lizard")
                elif self.player_one.chosen_gesture == "lizard" and self.ai.chosen_gesture == "paper":
                    self.ai_chosen()
                    self.player_one_win += 1
                    print("lizard eats paper")
                elif self.player_one.chosen_gesture == "lizard" and self.ai.chosen_gesture == "spock":
                    self.ai_chosen()
                    self.player_one_win += 1
                    print("lizard poisons spock")
                elif self.player_one.chosen_gesture == "lizard" and self.ai.chosen_gesture == "lizard":
                    self.ai_chosen()
                    self.draw += 1
                    print("draw")
                elif self.player_one.chosen_gesture == "spock" and self.ai.chosen_gesture == "rock":
                    self.ai_chosen()
                    self.player_one_win += 1
                    print("spock smashes rock")
                elif self.player_one.chosen_gesture == "spock" and self.ai.chosen_gesture == "sissors":
                    self.ai_chosen()
                    self.player_one_win += 1
                    print("spock smashes sissors")
                elif self.player_one.chosen_gesture == "spock" and self.ai.chosen_gesture == "paper":
                    self.ai_chosen()
                    self.ai_win += 1
                    print("paper confuses spock")
                elif self.player_one.chosen_gesture == "spock" and self.ai.chosen_gesture == "lizard":
                    self.ai_chosen()
                    self.ai_win += 1
                    print("lizard poisons spock")
                elif self.player_one.chosen_gesture == "spock" and self.ai.chosen_gesture == "spock":
                    self.ai_chosen()
                    self.draw += 1
                    print("draw")
        

    def display_winner(self):
        if self.player_one_win == 2:
            print(f"{self.player_one.name} wins the game")

        elif self.player_two_win == 2:
            print(f"{self.player_two.name} wins the game")

        elif self.ai_win == 2:
            print(f"{self.ai.name} wins the game")


import random

class Rps:

    choice_list = ['rock', 'paper', 'scissors'] 

    def __init__(self):
        pass
        
    def get_computer_choice(self,user_choice):
        computer_choice = random.choice(Rps.choice_list)
        print(f"You picked: {user_choice}. The computed picked {computer_choice}")
        self.get_winner(user_choice, computer_choice)
        

    def get_user_choice(self):
        while True:
            user_choice = str(input('please select Rock, Paper or Scissors or type "End Game" to end the game. Your choice: '))
            user_choice = user_choice.lower()
            if user_choice == 'end game':
                break
            elif user_choice not in Rps.choice_list:
                print('error, please try again: ')
            else:
                self.get_computer_choice(user_choice)

    def get_winner(self, user_choice, computer_choice):
        if computer_choice == user_choice:
            print("It's a draw!")
        elif computer_choice == 'rock' and user_choice == 'scissors':
            print('You lost')
        elif computer_choice == 'rock' and user_choice == 'paper':
            print('You Won')
        elif computer_choice == 'paper' and user_choice == 'rock':
            print('You lost')
        elif computer_choice == 'paper' and user_choice == 'scissors':
            print('You won')
        elif computer_choice == 'scissors' and user_choice == 'rock':
            print('You won')
        elif computer_choice == 'scissors' and user_choice == 'paper':
            print('You lost')
        else:
            print('No Result: Seems to be an error somewhere')

def play_rps():
    game = Rps()
    game.get_user_choice()




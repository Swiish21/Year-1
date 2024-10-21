import random

#This function is to get the user choice in the game rock paper scissors
def get_user_choice():
    user_choice = input("Enter Rock, Paper or Scissors: ").lower()
    while user_choice not in ["rock", "paper", "scisssors"]:
        print("Did you mean Rock, Paper or Scissors? ")
        user_choice = input("Enter Rock, Paper or Scissors: ").lower()
    return user_choice

#This function is to get computer choice in the game
def get_computer_choice():
    return random.choice(["rock", "paper", "scisssors"])

#This determines the winner between the computer and the user
def determine_winner(user_choice, computer_choice):
    print(f"You Chose {user_choice}")
    print(f"The computer chose {computer_choice}")

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "Rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer Wins"

def play_game():
    print("Welcome to Rock, Paper, Scissors")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()

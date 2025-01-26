import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play. Type 'exit' to quit.")

    choices = ['rock', 'paper', 'scissors']
    score = {"Player": 0, "Computer": 0}

    while True:
        player_choice = input("Your choice: ").lower()
        
        if player_choice == 'exit':
            print("Thanks for playing!")
            print(f"Final Score: Player {score['Player']} - {score['Computer']} Computer")
            break

        if player_choice not in choices:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'scissors' and computer_choice == 'paper') or \
             (player_choice == 'paper' and computer_choice == 'rock'):
            print("You win this round!")
            score["Player"] += 1
        else:
            print("Computer wins this round!")
            score["Computer"] += 1
        
        print(f"Current Score: Player {score['Player']} - {score['Computer']} Computer")
        print()

if __name__ == "__main__":
    rock_paper_scissors()

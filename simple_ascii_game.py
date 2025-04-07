import random

# ASCII art for each move
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Dictionary to map choices to art
ascii_art = {
    "rock": rock,
    "paper": paper,
    "scissors": scissors
}

# Get user input
human = input("Please enter rock, paper, or scissors: ").lower()

# Validate input
if human not in ascii_art:
    print("Invalid input! Please choose rock, paper, or scissors.")
else:
    # Computer randomly picks one
    computer = ['rock', 'paper', 'scissors']
    computer_decession = random.choice(computer)

    # Show choices with ASCII art
    print("\nYou chose:")
    print(ascii_art[human])

    print("Computer chose:")
    print(ascii_art[computer_decession])

    # Game logic
    if human == computer_decession:
        print("It's a tie! Play again.")
    elif (human == 'rock' and computer_decession == 'scissors') or \
         (human == 'scissors' and computer_decession == 'paper') or \
         (human == 'paper' and computer_decession == 'rock'):
        print("You won! 🎉")
    else:
        print("Computer has won the game 💻")
